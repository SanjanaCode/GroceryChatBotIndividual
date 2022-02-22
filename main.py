from app.bot import Bot

def main():
    bot = Bot()
    bot.detect_intent_texts("What is the cost of lemon?")


if __name__ == '__main__':
  main()
  #detect_intent_texts("When does the store close?")