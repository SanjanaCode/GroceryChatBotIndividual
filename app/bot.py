from google.cloud import dialogflow
from app.products.product_info import StoreInfoHandler
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
        #initiate conversation with customer
        self.start_conversation()

    def start_conversation(self):
        user_input = input("Hello, how can I help you?\n")
        while True:
            intent = self.detect_intent_texts(user_input)
            if intent == "Done-conversation":
                break
            else:
                print("Ok, here is the answer")
                user_input = input("What else can I help you?\n")
    
    def detect_intent_texts(self,text):

        text_input = dialogflow.TextInput(text=text, language_code=self.language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = self.session_client.detect_intent(
            request={"session": self.session, "query_input": query_input}
        )

        return response.query_result.intent.display_name