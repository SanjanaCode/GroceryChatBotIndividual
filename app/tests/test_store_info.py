import pytest
from app.products.product_info import StoreProductHandler
from app.products.database import STORE_INFO

@pytest.mark.store_info
class TestStoreInfo:

    @pytest.fixture
    def classTest(self):
        StoreProdHandler = StoreProductHandler()
        yield StoreProdHandler
        StoreProdHandler.dipose()

    
    def test_handler_address(self, classTest):
        message = "Where is the store?"
        expectedOutput = "It is {}".format(STORE_INFO["address"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_city(self, classTest):
        message = "Which city is the store at?"
        expectedOutput = "It is {}".format(STORE_INFO["city"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_province(self, classTest):
        message = "Which province is the store at?"
        expectedOutput = "It is {}".format(STORE_INFO["province"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_postal(self, classTest):
        message = "What is the postal code of the store?"
        expectedOutput = "It is {}".format(STORE_INFO["postal_code"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_country(self, classTest):
        message = "Which country is the store at?"
        expectedOutput = "It is {}".format(STORE_INFO["country"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_phone(self, classTest):
        message = "What is the store's phone number?"
        expectedOutput = "It is {}".format(STORE_INFO["phone"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_website(self, classTest):
        message = "What is the store's website?"
        expectedOutput = "It is {}".format(STORE_INFO["website"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_opening_hours(self, classTest):
        message = "What are the opening hours of the store?"
        expectedOutput = "It is {}".format(STORE_INFO["opening_hours"])
        assert(classTest.handle(message) == expectedOutput)