from app.products.database import MOCK_PRODUCT_DATA
import re
from app.products.base_handler import BaseHandler


class ProductInfoHandler(BaseHandler):
    def handle(self, user_input, productName, intent):
        return f'''
        Handle by product minibot
        Product name: {productName}
        Intent: {intent}
        User input: {user_input}
        '''