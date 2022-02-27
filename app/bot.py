from google.cloud import dialogflow
from app.products.product_info import *
from app.products.store_info import *
from app.concerns.other_concern import *
import random
import sys
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

    def start_conversation(self):
        print("""Bot: Hello, welcome to the official chatbot of Walmart. \nHere you can find information about our store, products \nand resolve any further concerns you have. \nHow can I help you today?""")
        #continuously take in user input (or maintain the conversation) 
        #until the user ends
        while True:
            user_input = input("You: ")
            #if user input is empty, prompt the input again
            if(not user_input):
                print("Bot: How can I help you?")
                continue
            #call dialogflow API to detect intent. If there is error, stop the program
            try:
                response = self.detect_intent_texts(user_input)
            except:
                print("Bot: There is an error on our end. Please try again later.")
                sys.exit()
            intent = response.intent.display_name            
            # if user greets (such as "hello"), then greet the user
            if(intent == "Default Welcome Intent"):
                print("Bot: " + response.fulfillment_text)
                continue
            # if user ends the converastion (such as "bye"), 
            # then end the conversation
            elif(intent == "Done-conversation"):
                print("Bot: Such a great pleasure to help you. Have a great day!")
                sys.exit()
            # if user asks about store, product, 
            # pass to product-info, store-info in route_to_handle. 
            # Set the undetected intent count to 0
            elif(intent == "product-info" or intent == "store-info"):
                print("Bot: " + self.route_to_handler(intent, user_input))
                self.undetected_intent_count = 0
            # if user asks for refund, 
            # direct to other concerns handler in route_to_handle
            elif(intent == "refund-request"):
                    print("Bot: " + response.fulfillment_text)
                    self.route_to_handler("other-concerns", user_input)
            # if intent can not be detected, increment times like this
            # if more than 3 times intent can't be detected, direct to other concerns handler
            else:    
                self.undetected_intent_count += 1
                if(self.undetected_intent_count == 3):
                    self.route_to_handler("other-concerns", user_input)
                    self.undetected_intent_count = 0
                else:
                    print("Bot: " + response.fulfillment_text)
                    continue
            # continue the conversation
            print("Bot: What else can I help you?")   
    
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
    def route_to_handler(self, intentDetected, userText):
        #If the question is about (detected intent) product info, direct it to the product information handler. Handler returns a response to user question. 
        #If the intent is not currently handled by the bot, create a new intent for it.
        if(intentDetected == "product-info"):
            if("product-info" not in self.intents):
                self.intents["product-info"] = ProductInfoHandler()
            response = self.intents["product-info"].handle(userText)

        #If the question is about (detected intent) product info, direct it to the product information handler. Handler returns a response to user question. 
        elif(intentDetected == "store-info"):
            if("store-info" not in self.intents):
                self.intents["store-info"] = StoreInfoHandler()
            response = self.intents["store-info"].handle(userText)

        #If intent cannot be detected or customer has further concerns, direct it to the other concerns handler. Handler returns a response to user question.
        else:
            if("other-concerns" not in self.intents):     
                self.intents["other-concerns"] = OtherConcerns() 
            response = self.intents["other-concerns"].handle()
        return response
