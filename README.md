# grocery-chat-bot

###### An assistant chatbot for a grocery store that helps answer customer queries.

The chatbot will greet the user, then answer their question about store/product information other, more complex concerns.

The chatbot will do so by doing a basic check of the user input, and redirecting the query to the appropriate mini-bot, where a more in-depth response will be handled. If the bot cannot decipher the user's message, they will be provided with the store's email, phone number, and hours to talk to a real employee.

## Setup

### Windows (PowerShell)

Creating virtual environment and install dependencies to run the bot:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Setting up the environment variables for the bot (Google cloud key).
```bash
$env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
```

### Unix (Bash)

Creating virtual environment and install dependencies to run the bot:

```bash
./install.sh
```

Setting up the environment variables for the bot (Google cloud key).
```bash
export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
```

## Run
```bash
python main.py
```

## Main Bot

The main bot will handle all inputs and ouputs from the user.

See in-depth documentation [here](app/greetings/README.md).

## Product & Store Mini-bot

This mini-bot will handle any question related to product price, stock, and store information. The bot first determines what topic is of interest (product or store information) and breaks the user's message down into keywords. The bot then compares these words and checks them in order to create the most appropriate response, and returns the response to the main bot.

See in-depth documentation [here](app/products/README.md).