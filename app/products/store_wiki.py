import requests
import json


class StoreSummary:
    """
    This class contains methods that handle all questions that relate to background information regarding the store (Walmart). 
    Attributes: None
    """
    def handle(self):
        """
        Handles questions about background information regarding the store. Specifically, the bot responds by providing a summary from wikipedia about the store.
        returns: Nothing
        """
        url = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=walmart"
            
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        result = json.loads(response.text)

        pageKey = list(result["query"]["pages"].keys())[0]
        print("Bot: ",result["query"]["pages"][pageKey]["extract"])

