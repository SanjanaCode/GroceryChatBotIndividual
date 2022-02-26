import pytest
import app.bot as Bot

class TestIntentRouting:

    def __init__(self):
        self.bot = Bot()

    def test_detect_intent_texts(self):
        assert self.bot.detect_intent_texts("hello") == "Default Welcome Intent", "Default Welcomr Intent failed"
        assert self.bot.detect_intent_texts("bye") == "Done-conversation", "Done-conversation failed"
        assert self.bot.detect_intent_texts("What is the price of an apple ?") == "product-info", "product-info failed"
        assert self.bot.detect_intent_texts("Where is your store ?") == "store-info", "store-address-info failed"
        assert self.bot.detect_intent_texts("When do you open ?") == "store-info", "store-time-info failed"
        assert self.bot.detect_intent_texts("I want to return my order") == "refund-request", "refund-request failed"
        assert self.bot.detect_intent_texts("") == "Default Fallback Intent", "Empty string failed"
    
