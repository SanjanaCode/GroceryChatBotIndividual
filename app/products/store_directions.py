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
        #Bot asks for user location 
        print("Bot: Please type your street number, street name, city, province")
        address = input("You: ")

        #format user's location in a way that the API request can understand.
        address = address.replace(',', ' + ')
        #get API request using the below URL. 'destination' parameter is the store address while origin parameter is the user's location.
        url = "https://maps.googleapis.com/maps/api/directions/json?origin="+address+"&destination=123+Main Street+Toronto+Ontario&key=AIzaSyCfc7KLR666d1byzIGuO6FaWpmtFO3zc1w"
        
        payload={}
        headers = {}

        #response for the request is returned as a json file.
        response = requests.request("GET", url, headers=headers, data=payload)
        #convert json into a python dictionary
        result = json.loads(response.text)

        #extract the total distance from user location to store
        distance = result["routes"][0]["legs"][0]["distance"]["text"]

        #extract the total drive time from user location to store
        travelTime = result["routes"][0]["legs"][0]["duration"]["text"]
        
        print("Bot: The store is ",distance," from your start location and under normal traffic condtions, the time taken to drive from your start location to the store is ",travelTime,".")
      
       

    