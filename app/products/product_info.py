from app.products.database import MOCK_PRODUCT_DATA
import re
from app.products.base_handler import BaseHandler


class ProductInfoHandler(BaseHandler):
    """
    A class used to represent a mini-bot to handle product queries.
    """

    def __init__(self) -> None:
        super().__init__()

    def create_match_paterns(self):
        # Product-related patterns
        self.price_pattern = re.compile(
            r"(price|cost|how much|money)", re.IGNORECASE)
        self.stock_pattern = re.compile(r"(stock|how many|amount)", re.IGNORECASE)
        self.nutrition_pattern = re.compile(
            r"(calories|protein|carbs|carbohydrates|sugar|fat|nutrition|nutritional|weight|health|healthy)", re.IGNORECASE)

    def dispose(self):
        super().dispose()

    def handle(self, message: str) -> str:
        # Call parser
        kwargs = self.parse(message=message)

        # If there is a topic detected, we find the response
        # By calling the handler with the message (for convenience) and its necessary arguments
        response = None
        if kwargs:
            response = self.handle_product_info(message, **kwargs)

            return response

    def parse(self, message: str) -> dict:
        request = None

        # Check for keywords for prices
        if self.nutrition_pattern.search(message):
            request = "nutrition"
        elif self.price_pattern.search(message):
            request = "price"
        elif self.stock_pattern.search(message):
            request = "stock"

        # If the request is truly about product
        if request:
            id = None
            for prod in MOCK_PRODUCT_DATA:
                prod_name = prod["name"]
                prod_id = prod["id"]
                prod_names = prod["names"]

                if prod_name in message or prod_id in message or prod_names in message:
                    id = prod["id"]

        return {"request": request, "id": id} if request else None

    def handle_product_info(self, message=None, **kwargs) -> str:
        # kwargs are arguments such as product_name, price, operators (<. >)
        # This really depends on how you define your parser
        prod_id = kwargs["id"]

        # Get the product information
        products = self.db.get_product("id", prod_id)

        # Since id is unique, we can assume there is only one product
        product = products[0]

        reply = None

        prod_msg_type = kwargs.get("request")
        if prod_msg_type == "price":
            reply = "%s cost $%s %s." % (
                product['names'].capitalize(), product['price'], product['price_scale'])
        elif prod_msg_type == "stock":
            if product['in_stock']:
                reply = "%s are in stock." % (product['names'].capitalize())
            else:
                reply = "%s are out of stock." % (
                    product['names'].capitalize())
        elif prod_msg_type == "nutrition":
            reply = "%s Nutrition Facts: Calories = %s, Protein = %s, Carbs = %s, Sugar = %s, Fat = %s." % (
                product['name'].capitalize(), product['calories'], product['protein'], product['carbs'], product['sugar'], product['fat'])

        return reply