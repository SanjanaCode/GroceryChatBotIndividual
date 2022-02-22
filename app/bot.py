class Bot:

    # def __init__(self):
    #     self.greeting()

    # def greeting(self):
    #     print("Hi!")
    #     options = "Please choose from one of the following options:\n a)Store information\n b)Product information\n c)Other concerns\n d)Exit"
    #     while(True):
    #         print(options)
    #         userInput = input().lower()
    #         if(userInput not in ["a","b","c","d","a)","b)","c)","d)"]):
    #             print("Incorrect input! Please enter a,b or c: ")
    #         else:
    #             if(userInput in ["a","a)"]):
    #                 self.getStoreInfo()
    #             elif(userInput in ["b","b)"]):
    #                 self.getProductInfo()
    #             elif(userInput in ["c","c)"]):
    #                 self.getCustomerService()
    #             else:
    #                 print("Goodbye!")
    #                 break
    #             print("Is there anything else I could help you with?")



    # def getStoreInfo(self):
    #     print("store info")

    # def getCustomerService(self):
    #     print("customer service info")
    
    # def getProductInfo(self):
    #     print("product info")

    project_id = "grocery-chat-bot"
    session_id = "test"
    texts = "Hello"
    def detect_intent_texts(text, project_id = "grocery-chat-bot", session_id = "test", language_code = "en-US"):
        """Returns the result of detect intent with texts as inputs.

        Using the same `session_id` between requests allows continuation
        of the conversation."""
        from google.cloud import dialogflow

        session_client = dialogflow.SessionsClient()

        session = session_client.session_path(project_id, session_id)
        print("Session path: {}\n".format(session))

        text_input = dialogflow.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        print("=" * 20)
        print("Query text: {}".format(response.query_result.query_text))
        print(
            "Detected intent: {} (confidence: {})\n".format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence,
            )
        )
        print("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))

