from app.bot import Bot
from app.products.store_directions import *
from app.products.store_wiki import *
# from dialogflow_migration.bot import Bot

def main():
    bot = Bot()
    #initiate conversation with customer
    bot.start_conversation()


if __name__ == '__main__':
  main()