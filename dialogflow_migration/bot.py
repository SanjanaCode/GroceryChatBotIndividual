from google.cloud import dialogflow
from dialogflow_migration.products.product_info import *
from dialogflow_migration.products.store_info import *
from app.concerns.other_concern import *
import random
import sys
class Bot:
    def __init__(self):
        project_id = "grocery-chat-bot-test-def-qvwt"
        #generate unique session id for each conversation. 
        # Session id is for continuation of conversation
        #TODO: create unique number
        self.session_id = random.randint(1, 100)
        #one session is only for one customer
        self.session_client = dialogflow.SessionsClient()
        self.language_code = "en-US"
        self.session = self.session_client.session_path(project_id, self.session_id)
        #current intents the bot handle
        self.intents = {}
        #keep track of times the intent is not detected
        self.undetected_intent_count = 0

    def start_conversation(self):
        while True:
            user_input = input("You: ")
            try:
                response = self.detect_intent_texts(user_input)
            except:
                print("Bot: There is an error on our end. Please try again later.")
                sys.exit()
            intent = response.intent.display_name     
            if(intent == "product-price" or intent == "product-stock" or intent == "product-nutrition"):
                productName = response.parameters["product-name"]
                print("json object")
                print("{")
                print(response)
                print("}")
                print("Bot: " + self.route_to_handler(productName = productName, intent = intent))
                self.undetected_intent_count = 0
            # if user asks about store, 
            # pass to store-info in route_to_handle. 
            # Set the undetected intent count to 0
            elif(intent == "store-info"):
                print("Bot: " + self.route_to_handler(intent = intent, user_input = user_input))
                self.undetected_intent_count = 0
            
    
    def detect_intent_texts(self,text):
        try:
            # Process text_input
            text_input = dialogflow.TextInput(text=text, language_code=self.language_code)
            # Call Dialogflow API
            query_input = dialogflow.QueryInput(text=text_input)

            response = self.session_client.detect_intent(
                request={"session": self.session, "query_input": query_input}
            )
            return response.query_result
        except:
            raise Exception("Dialogflow API error")

    #Based on intent, route to appropriate handler and return response for user input.
    def route_to_handler(self, **kwargs):
        #If the question is about (detected intent) product info, direct it to the product information handler. Handler returns a response to user question. 
        #If the intent is not currently handled by the bot, create a new intent for it.
        if("product" in kwargs["intent"]):
            if("product-info" not in self.intents):
                self.intents["product-info"] = ProductInfoHandler()
            response = self.intents["product-info"].handle(kwargs["productName"], kwargs["intent"])

        #If the question is about (detected intent) product info, direct it to the product information handler. Handler returns a response to user question. 
        elif("store" in kwargs["intent"]):
            if("store-info" not in self.intents):
                self.intents["store-info"] = StoreInfoHandler()
            response = self.intents["store-info"].handle(kwargs["user_input"])
        return response