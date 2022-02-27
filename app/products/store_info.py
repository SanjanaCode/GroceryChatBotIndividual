import os
from typing import OrderedDict
from app.products.database import SQLiteDatabase, DatabaseType, MOCK_PRODUCT_DATA, STORE_INFO
import re
from collections import OrderedDict

class StoreInfoHandler:
    """
    A class used to represent a mini-bot to handle product queries.

    Attributes
    ----------
    runtime_mode : str
        The environment that the bot is running in (i.e. DEV or PRODUCTION).

    handler_map : dict
        The mapping from sub-topic and corresponding handler.

    Methods
    -------
    handle(message: str)
        Handle the message and return the proper response.
    """
    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the ProductHandler object.
        """
        # Set the operation mode (i.e. DEV or PRODUCTION)
        self.runtime_mode = os.getenv("PYTHON_ENV", "DEV")

        # Create pattern matches
        self.create_match_paterns()

        # Initialize a mock database if development environment
        if self.runtime_mode == "DEV":
            self.db = SQLiteDatabase(DatabaseType.MEMORY)
            self.db.connect()  # Start a connection
            self.db.init_database()  # Initialize the database
        else:
            self.db = None
    
    def create_match_paterns(self):
        """
        This method is called when the class is initialized.
        """
        # Store-related patterns
        self.location_pattern = re.compile(
            r"(where|location|address|street)", re.IGNORECASE)
        self.opening_pattern = re.compile(
            r"(when|open|close|opening|closing|hours)", re.IGNORECASE)
        self.phone_pattern = re.compile(r"(phone|number)", re.IGNORECASE)
        self.website_pattern = re.compile(r"(website|url|web)", re.IGNORECASE)
        self.city_pattern = re.compile(r"(city|town)", re.IGNORECASE)
        self.province_pattern = re.compile(r"(province|state)", re.IGNORECASE)
        self.country_pattern = re.compile(r"(country)", re.IGNORECASE)
        self.postal_code_pattern = re.compile(r"(postal|zip)", re.IGNORECASE)

    def dispose(self):
        """
        Call this methods to release any resources with this minibot (i.e. database connection).
        """
        self.db.close()

    def handle(self, message: str) -> str:
        """
        The entry point of the mini-bot. 

        Main bot will call this method to pass in the message to process.

        Parameters
        ----------

        message: str
            The message that the user sends to the bot.


        Returns
        ----------
        response: str
            The response string to the request message
        """

        response = None

        matched, name, kargs = self.parse_store_info(message=message)
        
        # If there is a topic detected, we find the response
        # By calling the handler with the message (for convenience) and its necessary arguments
        
        if matched:
            response = self.handle_store_info(message, **kargs)

        return response

    # @Quan @Paul
    # TODO: Implement helper method to parse store information.
    # This method should return a tuple of (boolean, str, dict).
    # The first item indicates whether this request is about store information.
    # If false, the other items must be None.
    def parse_store_info(self, message) -> tuple:
        is_store = False
        store_words = {"request": None}

        if self.location_pattern.search(message):
            store_words["request"] = "address"
        elif self.opening_pattern.search(message):
            store_words["request"] = "opening_hours"
        elif self.phone_pattern.search(message):
            store_words["request"] = "phone"
        elif self.website_pattern.search(message):
            store_words["request"] = "website"
        elif self.city_pattern.search(message):
            store_words["request"] = "city"
        elif self.province_pattern.search(message):
            store_words["request"] = "province"
        elif self.postal_code_pattern.search(message):
            store_words["request"] = "postal_code"
        elif self.country_pattern.search(message):
            store_words["request"] = "country"

         # If the request is truly about store
        if store_words["request"] is not None:
            is_store = True

        return (is_store, "store_info", store_words)

    # @Quan @Paul
    # TODO: Implement the method to return proper response for product information.
    # Note: This is the signature for all handler methods.
    def handle_store_info(self, message=None, **kwargs) -> str:
        # kwargs are arguments such as product_name, price, operators (<. >)
        # This really depends on how you define your parser
        reply = "It is {}".format(STORE_INFO[kwargs["request"]])
        return reply