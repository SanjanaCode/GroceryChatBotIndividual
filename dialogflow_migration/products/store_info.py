from app.products.database import STORE_INFO
from app.products.base_handler import BaseHandler
import re


class StoreInfoHandler(BaseHandler):
    def handle(self, user_input, intent):
        return f'''
        Handle by store minibot
        Intent: {intent}
        User input: {user_input}
        '''
