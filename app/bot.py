from google.cloud import dialogflow
from app.products.product_info import *
from app.concerns.further_concern import *
import random
class Bot:
    def __init__(self):
        project_id = "grocery-chat-bot"
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
        #initiate conversation with customer
        self.start_conversation()

    def start_conversation(self):
        print("Hello, how can I help you?")
        #continuously take in user input (or maintain the conversation) 
        #until the user ends
        while True:
            user_input = input()
            #call dialogflow API to detect intent
            response = self.detect_intent_texts(user_input)
            intent = response.intent.display_name            
            # if user greets (such as "hello"), then greet the user
            if(intent == "Default Welcome Intent"):
                print(response.fulfillment_text)
                continue
            # if user ends the converastion (such as "bye"), 
            # then close the conversation
            elif(intent == "Done-conversation"):
                print("Such a great pleasure to help you. Have a great day!")
                break
            # if user asks about store, product, 
            # pass to product-info, store-info in route_to_handle. 
            # Set the undetected intent count to 0
            elif(intent == "product-info" or intent == "store-info"):
                self.route_to_handler(intent, user_input)
                self.undetected_intent_count = 0
            # if user asks for refund, 
            # direct to other concerns handler in route_to_handle
            elif(intent == "refund-request"):
                    print(response.fulfillment_text)
                    self.route_to_handler("other-concerns", user_input)
            # if intent can not be detected, increment times like this
            # if more than 3 times intent can't be detected, direct to other concerns handler
            else:    
                self.undetected_intent_count += 1
                if(self.undetected_intent_count == 3):
                    self.route_to_handler("other-concerns", user_input)
                    self.undetected_intent_count = 0
                else:
                    print(response.fulfillment_text)
                    continue
            # continue the conversation
            print("What else can I help you?")   
    
    def detect_intent_texts(self,text):
        # Process text_input
        text_input = dialogflow.TextInput(text=text, language_code=self.language_code)
        # Call Dialogflow API
        query_input = dialogflow.QueryInput(text=text_input)

        response = self.session_client.detect_intent(
            request={"session": self.session, "query_input": query_input}
        )

        return response.query_result

    #Based on intent, route to appropriate handler
    def route_to_handler(self, intentDetected ,userText):
        #If the question is about (detected intent) product info, direct it to the product information handler.  
        #If the intent is not currently handled by the bot, create a new intent for it.
        if(intentDetected == "product-info"):
            if("product-info" not in self.intents):
                self.intents["product-info"] = ProductInfo()
            self.intents["product-info"].prodHandler(userText)
        elif(intentDetected == "store-info"):
            if("store-info" not in self.intents):
                self.intents["store-info"] = StoreInfo()
            self.intents["store-info"].storeHandler(userText)
        #If intent cannot be detected or customer has further concerns, direct it to the other concerns handler   
        else:
            #if object for other-concerns is not already in the intents map, create a new object. Else invoke handler using existing object. 
            if("other-concerns" not in self.intents):     
                self.intents["other-concerns"] = OtherConcerns() 
            self.intents["other-concerns"].concernsHandler(userText)
