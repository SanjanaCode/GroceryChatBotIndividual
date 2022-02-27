import pytest
from app.bot import Bot
from google.cloud import dialogflow

@pytest.mark.intentDetectionTest
class TestIntentRouting:

    @pytest.fixture
    def bot(self):
        return Bot()

    def test_detect_intent_texts(self,bot):
        assert bot.detect_intent_texts("hello").intent.display_name == "Default Welcome Intent", "Default Welcome Intent failed"
        assert bot.detect_intent_texts("bye").intent.display_name == "Done-conversation", "Done-conversation failed"
        assert bot.detect_intent_texts("What is the price of an apple ?").intent.display_name == "product-info", "product-info failed"
        assert bot.detect_intent_texts("Where is your store ?").intent.display_name == "store-info", "store-address-info failed"
        assert bot.detect_intent_texts("When do you open ?").intent.display_name == "store-info", "store-time-info failed"
        assert bot.detect_intent_texts("I want to return my order").intent.display_name == "refund-request", "refund-request failed"
    
