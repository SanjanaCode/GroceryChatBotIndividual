import pytest
from app.products.product_info import StoreProductHandler
from app.products.database import MOCK_PRODUCT_DATA


class TestProductInfo:
    def test_handler_pricebanana(self):
        classTest = StoreProductHandler()
        message = "What is the price of a banana?"
        expectedOutput = "%s cost $%s %s." % (MOCK_PRODUCT_DATA[0]["names"].capitalize(), MOCK_PRODUCT_DATA[0]["price"], MOCK_PRODUCT_DATA[0]["price_scale"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_stockbanana(self):
        classTest = StoreProductHandler()
        message = "How many bananas do you have?"
        expectedOutput = "{} are in stock.".format(MOCK_PRODUCT_DATA[0]["names"].capitalize())
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_priceberry(self):
        classTest = StoreProductHandler()
        message = "How much do strawberries cost?"
        expectedOutput = "%s cost $%s %s." % (MOCK_PRODUCT_DATA[1]["names"].capitalize(), MOCK_PRODUCT_DATA[1]["price"], MOCK_PRODUCT_DATA[1]["price_scale"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_stockberry(self):
        classTest = StoreProductHandler()
        message = "Are strawberries in stock?"
        expectedOutput = "{} are in stock.".format(MOCK_PRODUCT_DATA[1]["names"].capitalize())
        assert(classTest.handle(message) == expectedOutput)

    