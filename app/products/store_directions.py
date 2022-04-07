import requests
import json

class StoreDirections:
    """
    This class contains methods that handle all questions that relate to directions to the store, specifically how far away and how long it takes to reach the store from user's location.
    Attributes: None
    """
    def handle(self):
        """
        Handles questions regarding the distance and time taken to reach store. Specifically, based a user location, the bot responds by providing the distance to the store and the drive time  under normal traffic conditions.
        returns: Nothing
        """
        print("Bot: Please type your street number, street name, city, province")
        address = input("You: ")
        address = address.replace(',', ' + ')
        url = "https://maps.googleapis.com/maps/api/directions/json?origin=123+Main Street+Toronto+Ontario&destination="+address+"&key=AIzaSyCfc7KLR666d1byzIGuO6FaWpmtFO3zc1w"
        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        result = json.loads(response.text)
        distance = result["routes"][0]["legs"][0]["distance"]["text"]
        travelTime = result["routes"][0]["legs"][0]["duration"]["text"]
        print("Bot: The store is ",distance," from your start location and under normal traffic condtions, the time taken to drive from your start location to the store is ",travelTime,".")
      
       

    