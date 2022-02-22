from google.cloud import dialogflow
from app.products.product_info import *
import random
class Bot:
    def __init__(self):
        project_id = "grocery-chat-bot"
        #generate unique session id for each conversation. Session id is for continuation of conversation
        #TODO: create unique number
        self.session_id = random.randint(1, 100)
        #one session is only for one customer
        self.session_client = dialogflow.SessionsClient()
        self.language_code = "en-US"
        self.session = self.session_client.session_path(project_id, self.session_id)
        #current intents the bot handle
        self.intents = {}
        #initiate conversation with customer
        self.start_conversation()

    def start_conversation(self):
        print("Hello, how can I help you?\n")
        #continuously take in user input (or maintain the conversation) until the user ends
        while True:
            user_input = input()
            response = self.detect_intent_texts(user_input)
            intent = response.intent.display_name
            # if user ends the converastion (such as "bye"), then close the conversation
            # if user greets (such as "hello"), then greet the user
            # if user asks about store, product, pass to route_to_handle
            if intent == "Done-conversation":
                break
            elif intent == "Default Welcome Intent" or intent == "Default Fallback Intent":
                print(response.fulfillment_text)
            else:
                self.route_to_handler(intent, user_input)
                print("What else can I help you?\n")
    
    def detect_intent_texts(self,text):

        # Process text_input
        text_input = dialogflow.TextInput(text=text, language_code=self.language_code)
        # Call Dialogflow API
        query_input = dialogflow.QueryInput(text=text_input)

        response = self.session_client.detect_intent(
            request={"session": self.session, "query_input": query_input}
        )

        return response.query_result

    def route_to_handler(self, intentDetected ,userText):
        #If the question is about (detected intent) product info, direct it to the product information handler.  
        #If the intent is not currently handled by the bot, create a new intent for it.
        if(intentDetected == "product-info"):
            if("product-info" not in self.intents):
                self.intents["product-info"] = ProductInfo()
            self.intents["product-info"].prodHandler(userText)
        else:
            if("store-info" not in self.intents):
                self.intents["store-info"] = StoreInfo()
            self.intents["store-info"].storeHandler(userText)
