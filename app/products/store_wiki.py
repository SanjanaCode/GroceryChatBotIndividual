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
        #get API request using the below URL. 'title' parameter takes the value for which wikipedia summary needs to be extracted.
        url = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=walmart"
            
        payload={}
        headers = {}

        #response for the request is returned as a json file.
        response = requests.request("GET", url, headers=headers, data=payload)
        #convert json into a python dictionary
        result = json.loads(response.text)

        #First extract page key for the page which contains the wikipedia information and then extract the first paragraph from it. 
        pageKey = list(result["query"]["pages"].keys())[0]
        
        print("Bot: ",result["query"]["pages"][pageKey]["extract"])

