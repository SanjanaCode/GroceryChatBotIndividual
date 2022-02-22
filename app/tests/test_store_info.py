import pytest
from app.products.product_info import StoreProductHandler
from app.products.database import STORE_INFO


class TestStoreInfo:
    # def test_handler_name(self):
    #     classTest = StoreProductHandler()  # haven't added handler for name yet
    #     message = "What is the name of the store?"
    #     expectedOutput = "It is {}".format(STORE_INFO["name"])
    #     assert(classTest.handle(message) == expectedOutput)
    def test_handler_address(self):
        classTest = StoreProductHandler()
        message = "Where is the store?"
        expectedOutput = "It is {}".format(STORE_INFO["address"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_city(self):
        classTest = StoreProductHandler()
        message = "Which city is the store at?"
        expectedOutput = "It is {}".format(STORE_INFO["city"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_province(self):
        classTest = StoreProductHandler()
        message = "Which province is the store at?"
        expectedOutput = "It is {}".format(STORE_INFO["province"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_postal(self):
        classTest = StoreProductHandler()
        message = "What is the postal code of the store?"
        expectedOutput = "It is {}".format(STORE_INFO["postal_code"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_country(self):
        classTest = StoreProductHandler()
        message = "Which country is the store at?"
        expectedOutput = "It is {}".format(STORE_INFO["country"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_phone(self):
        classTest = StoreProductHandler()
        message = "What is the store's phone number?"
        expectedOutput = "It is {}".format(STORE_INFO["phone"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_website(self):
        classTest = StoreProductHandler()
        message = "What is the store's website?"
        expectedOutput = "It is {}".format(STORE_INFO["website"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_opening_hours(self):
        classTest = StoreProductHandler()
        message = "What are the opening hours of the store?"
        expectedOutput = "It is {}".format(STORE_INFO["opening_hours"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_price_range(self):
        classTest = StoreProductHandler()
        message = "What is the store's price range?"
        expectedOutput = "It is {}".format(STORE_INFO["price"])
        assert(classTest.handle(message) == expectedOutput)
