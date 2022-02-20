import os

# @Quan @Paul @Thuan
# TODO: Add mock data if needed
mock_product_data = [
    {"id": "4011", "name": "banana", "names": "bananas", "price": "0.67",
     "price_scale": "per kg", "in_stock": True},
    {"id": "3022", "name": "strawberry", "names": "strawberries", "price": "3.99",
     "price_scale": "per box", "in_stock": True},
]


class StoreProductHandler:
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

        # Initialize the mapping from sub-topic and handler
        self.handler_map = {
            "product_info": self.handle_product_info,
            "store_info": self.handle_store_info
        }

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

        # Parse the query
        topic, kargs = self.parse_query(message=message)

        # Get the handler
        handler = self.handler_map.get(topic)

        # If there is a topic detected, we find the response
        # By calling the handler with the message (for convenience) and its necessary arguments
        if handler:
            response = handler(message, kargs)

        return response

    def parse_query(self, message: str) -> tuple:
        """
        Method to parse the query and return the a tuple of (topic_name, arguments for handler).

        Parameters
        ----------

        message : str
            The message that the user sends to the bot.
        """

        # Define a topic name and arguments for handler
        name = None
        kwargs = {}

        # Check if it a product query
        matched, name, kwargs = self.parse_product_info(message=message)

        # Check if it is a store query
        # This only runs if product request parser returns false on status.
        if not matched:
            _, name, kwargs = self.parse_store_info(message=message)

        return name, kwargs

    # @Paul @Thuan
    # TODO: Implement helper method to parse product information.
    # This method should return a tuple of (boolean, str, dict).
    # The first item indicates whether this request is about product information.
    def parse_product_info(self, message) -> tuple:
        is_prod = False
        prod_words = {"request": None, "product_name": None}
        if "price" or "cost" or "how much" in message:
            prod_words["request"] = "price"
            is_prod = True
        elif "stock" or "how many" in message:
            prod_words["request"] = "stock"
            is_prod = True
        
        for prod in mock_product_data:
            if prod["id"] or prod["name"] or prod["names"] in message:
                prod_words["product_name"] = prod["names"]

        return (is_prod, "product_info", prod_words)

    # @Quan @Paul
    # TODO: Implement helper method to parse store information.
    # This method should return a tuple of (boolean, str, dict).
    # The first item indicates whether this request is about store information.
    # If false, the other items must be None.
    def parse_store_info(self, message) -> tuple:
        return (False, "store_info", {})

    # @Paul @Thuan
    # TODO: Implement the method to return proper response for product information.
    # Note: This is the signature for all handler methods.
    # If false, the other items must be None.
    def handle_product_info(self, message=None, **kwargs) -> str:
        # kwargs are arguments such as product_name, price, operators (<. >)
        # This really depends on how you define your parser
        prod_price, prod_scale, prod_stock, reply = None

        prod_name = kwargs.get("product_name")
        for prod in mock_product_data:
            if prod["names"] == prod_name:
                prod_price = prod["price"]
                prod_scale = prod["price_scale"]
                prod_stock = prod["in_stock"]
                break
        
        prod_msg_type = kwargs.get("requests")
        if prod_msg_type == "price":
            reply = "%s cost $%s %s." % (prod_name.capitalize(), prod_price, prod_scale)
        elif prod_msg_type == "stock":
            if prod_stock == True:
                reply = "%s are in stock." % (prod_name.capitalize())
            else:
                reply = "%s are out of stock." % (prod_name.capitalize())
        
        return reply

    # @Quan @Paul
    # TODO: Implement the method to return proper response for product information.
    # Note: This is the signature for all handler methods.
    def handle_store_info(self, message=None, **kwargs) -> str:
        # kwargs are arguments such as product_name, price, operators (<. >)
        # This really depends on how you define your parser
        pass

    # @Thuan @Paul @Quan
    # TODO: Once database is improved for use, we can have a more flexible way to retrieve data.
    # For now, only 1 attribute can be matched at a time.
    def get_product(self, attr: str, value=None) -> list:
        """
        Method to get the first product that has a matching attribute value.

        This is equivalent to SELECT * WHERE attr = value.

        Parameters
        ----------

        attr: str
            The attribute name.

        value: any
            The value to match for specified attribute.


        Returns
        ----------

        product: dict
            The information about the product.
        """

        # Define a list
        products = []

        # If in development environment
        if self.runtime_mode == "DEV":
            # Loop to search
            for mock_product in mock_product_data:
                if mock_product[attr] == value:
                    products.append(mock_product)

            return products
        else:
            # @Thuan
            # TODO: Implement database connection to retrieve necessary data
            return products
