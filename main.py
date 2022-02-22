from app.bot import Bot

def main():
    bot = Bot()
    bot.route_to_handler("product-info","what is apples?")


if __name__ == '__main__':
  main()
  #detect_intent_texts("When does the store close?")