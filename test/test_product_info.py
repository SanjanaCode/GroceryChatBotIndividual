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

    def test_handler_stockapple(self, classTest):
        message = "How many apples do you have?"
        expectedOutput = "{} are in stock.".format(MOCK_PRODUCT_DATA[2]["names"].capitalize())
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_priceberry(self, classTest):
        message = "How much do strawberries cost?"
        expectedOutput = "%s cost $%s %s." % (MOCK_PRODUCT_DATA[1]["names"].capitalize(), MOCK_PRODUCT_DATA[1]["price"], MOCK_PRODUCT_DATA[1]["price_scale"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_stockpear(self, classTest):
        message = "Are pears in stock?"
        expectedOutput = "{} are out of stock.".format(MOCK_PRODUCT_DATA[3]["names"].capitalize())
        assert(classTest.handle(message) == expectedOutput)

@pytest.mark.prod_info
class TestNutritionInfo:
    @pytest.fixture
    def classTest(self):
        storeProdHandler = ProductInfoHandler()
        yield storeProdHandler
        storeProdHandler.dispose()

    def test_handler_nutrition_banana(self, classTest):
        message = "What is the nutritional value of a banana?"
        expectedOutput = "%s Nutrition Facts: Calories = %s, Protein = %s, Carbs = %s, Sugar = %s, Fat = %s." % (MOCK_PRODUCT_DATA[0]["name"].capitalize(), MOCK_PRODUCT_DATA[0]["calories"], MOCK_PRODUCT_DATA[0]["protein"], MOCK_PRODUCT_DATA[0]["carbs"], MOCK_PRODUCT_DATA[0]["sugar"], MOCK_PRODUCT_DATA[0]["fat"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_nutrition_strawberry(self, classTest):
        message = "How many calories is in a strawberry?"
        expectedOutput = "%s Nutrition Facts: Calories = %s, Protein = %s, Carbs = %s, Sugar = %s, Fat = %s." % (MOCK_PRODUCT_DATA[1]["name"].capitalize(), MOCK_PRODUCT_DATA[1]["calories"], MOCK_PRODUCT_DATA[1]["protein"], MOCK_PRODUCT_DATA[1]["carbs"], MOCK_PRODUCT_DATA[1]["sugar"], MOCK_PRODUCT_DATA[1]["fat"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_nutrition_apple(self, classTest):
        message = "How much carbs is in an apple?"
        expectedOutput = "%s Nutrition Facts: Calories = %s, Protein = %s, Carbs = %s, Sugar = %s, Fat = %s." % (MOCK_PRODUCT_DATA[2]["name"].capitalize(), MOCK_PRODUCT_DATA[2]["calories"], MOCK_PRODUCT_DATA[2]["protein"], MOCK_PRODUCT_DATA[2]["carbs"], MOCK_PRODUCT_DATA[2]["sugar"], MOCK_PRODUCT_DATA[2]["fat"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_nutrition_pear(self, classTest):
        message = "What is the nutrition of a pear?"
        expectedOutput = "%s Nutrition Facts: Calories = %s, Protein = %s, Carbs = %s, Sugar = %s, Fat = %s." % (MOCK_PRODUCT_DATA[3]["name"].capitalize(), MOCK_PRODUCT_DATA[3]["calories"], MOCK_PRODUCT_DATA[3]["protein"], MOCK_PRODUCT_DATA[3]["carbs"], MOCK_PRODUCT_DATA[3]["sugar"], MOCK_PRODUCT_DATA[3]["fat"])
        assert(classTest.handle(message) == expectedOutput)

    def test_handler_nutrition_error(self, classTest):
        message = "What is the nutrition of anything?"
        try:
            reply = classTest.handle(message)
            pytest.fail("Expected exception not raised")
        except Exception as e:
            assert(str(e) == "list index out of range") # no item specified in the message

    