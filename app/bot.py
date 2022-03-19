from google.cloud import dialogflow
from app.products.product_info import *
from app.products.store_info import *
from app.concerns.other_concern import *
import random
import sys

class Bot:
    """
    This the main bot class that handles conversation with users.

    Parameters: None

    Attributes: 
        project_id: google project id of the agent
        session_id: unique session id for each conversation
        session_client: session client object for dialogflow
        language_code: language code for dialogflow, initially set to en-US
        session: session path for dialogflow
        intents: dictionary of current intents the bot handles
        undetected_intent_count: keep track of times the intent is not detected
    """
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
        self.intents = {}
        self.undetected_intent_count = 0

    def start_conversation(self):
        """
        Initiate conversation with user and maintain the conversation until user says bye.
        For each user input, detect intent and route to appropriate handler.

        Parameters: None

        Returns: None
        """
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
            # if user ends the conversation (such as "bye"), 
            # then end the conversation
            elif(intent == "Done-conversation"):
                print("Bot: Such a great pleasure to help you. Have a great day!")
                sys.exit()
            # if user asks about product, 
            # pass to store-info in route_to_handle. 
            # Set the undetected intent count to 0
            elif("product" in intent):# intent can be product-stock or product-nutrition or product-price
                productName = response.parameters["product-name"]
                print("Bot: " + self.route_to_handler(productName = productName, intent = intent))
                self.undetected_intent_count = 0 # reset the undetected intent count if bot already responded the intent
            # if user asks about store, 
            # pass to store-info in route_to_handle. 
            # Set the undetected intent count to 0
            elif(intent == "store-info"):
                print("Bot: " + self.route_to_handler(intent = intent, user_input = user_input))
                self.undetected_intent_count = 0 # reset the undetected intent count if bot already responded the intent
            # if user asks for exchange or refund or feedback, 
            # direct to other concerns handler in route_to_handle
            elif(intent == "exchange-request" or intent == "refund-request" or intent == "feedback"):
                    self.route_to_handler(sentimentScore = response.sentiment_analysis_result.query_text_sentiment.score, intent = intent)
                    self.undetected_intent_count = 0 # reset the undetected intent count if bot already responded the intent
            # if the bot doesn't understand the user intent, 
            # then ask for rephrase and increment the undetected intent count
            # if the bot doesn't understand the user intent for 3 times,
            # then set sentiment score to 0 and pass to other concerns handler in route_to_handle               
            else:    
                self.undetected_intent_count += 1
                if(self.undetected_intent_count == 3):
                    self.route_to_handler(sentimentScore = 0, intent = intent)
                    self.undetected_intent_count = 0 # reset the undetected intent count if bot already responded the intent
                else:
                    print("Bot: " + response.fulfillment_text)
                    continue
            # continue the conversation
            print("Bot: What else can I help you?")   
    
    def detect_intent_texts(self,text):
        """
        Takes user input and makes a request to dialogflow api to detect intent.

        Parameters:
            text: user input

        Returns: query_result from json object received from dialogflow

        Raises: exception with text "Dialogflow API error" if cannot connect to dialogflow
        """
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
        """
        Takes intent name and necessary parameters and routes to appropriate handler.
        Handlers include: product-info, store-info, other-concerns.

        Parameters:
            intent: name of intent
            productName: name of product. Only required if intent is about product
            user_input: user input. Only required if intent is about store
        
        Returns: text response from handlers
        """
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

        #If intent cannot be detected or customer has further concerns, direct it to the other concerns handler. Handler returns a response to user question.
        else:
            if("other-concerns" not in self.intents):     
                self.intents["other-concerns"] = OtherConcerns() 
            response = self.intents["other-concerns"].handle(kwargs["sentimentScore"], kwargs["intent"])
        return response
