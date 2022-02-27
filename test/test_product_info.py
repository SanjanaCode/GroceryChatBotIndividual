import pytest
from app.products.product_info import ProductInfoHandler
from app.products.database import MOCK_PRODUCT_DATA
@pytest.mark.prod_info

class TestProductInfo:
    @pytest.fixture
    def classTest(self):
        storeProdHandler = ProductInfoHandler()
        yield storeProdHandler
        storeProdHandler.dispose()

    def test_handler_pricebanana(self, classTest):
        message = "What is the price of a banana?"
        expectedOutput = "%s cost $%s %s." % (MOCK_PRODUCT_DATA[0]["names"].capitalize(), MOCK_PRODUCT_DATA[0]["price"], MOCK_PRODUCT_DATA[0]["price_scale"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_stockbanana(self, classTest):
        message = "How many bananas do you have?"
        expectedOutput = "{} are in stock.".format(MOCK_PRODUCT_DATA[0]["names"].capitalize())
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_priceberry(self, classTest):
        message = "How much do strawberries cost?"
        expectedOutput = "%s cost $%s %s." % (MOCK_PRODUCT_DATA[1]["names"].capitalize(), MOCK_PRODUCT_DATA[1]["price"], MOCK_PRODUCT_DATA[1]["price_scale"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_stockberry(self, classTest):
        message = "Are strawberries in stock?"
        expectedOutput = "{} are in stock.".format(MOCK_PRODUCT_DATA[1]["names"].capitalize())
        assert(classTest.handle(message) == expectedOutput)

    