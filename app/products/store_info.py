from app.products.database import STORE_INFO
from app.products.base_handler import BaseHandler
import re


class StoreInfoHandler(BaseHandler):
    """
    A class used to represent a mini-bot to handle store queries.
    """

    def __init__(self) -> None:
        super().__init__()

    def create_match_paterns(self):
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
        super().dispose()

    def handle(self, message: str) -> str:
        # Call parser
        kwargs = self.parse(message=message)

        # If there is a topic detected, we find the response
        # By calling the handler with the message (for convenience) and its necessary arguments
        response = None
        if kwargs:
            response = self.handle_store_info(message, **kwargs)

        return response

    def parse(self, message) -> dict:
        request = None

        if self.location_pattern.search(message):
            request = "address"
        elif self.opening_pattern.search(message):
            request = "opening_hours"
        elif self.phone_pattern.search(message):
            request = "phone"
        elif self.website_pattern.search(message):
            request = "website"
        elif self.city_pattern.search(message):
            request = "city"
        elif self.province_pattern.search(message):
            request = "province"
        elif self.postal_code_pattern.search(message):
            request = "postal_code"
        elif self.country_pattern.search(message):
            request = "country"

        return {"request": request} if request else None

    def handle_store_info(self, message=None, **kwargs) -> str:
        # kwargs are arguments such as product_name, price, operators (<. >)
        # This really depends on how you define your parser
        reply = "It is {}".format(STORE_INFO[kwargs["request"]])
        return reply
