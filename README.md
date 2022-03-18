# grocery-chat-bot

###### An assistant chatbot for a grocery store that helps answer customer queries.

The chatbot will greet the user, then answer their question about store/product information or other, more complex concerns.

The chatbot will do so by doing a basic check of the user input, and redirecting the query to the appropriate mini-bot, where a more in-depth response will be handled. If the bot cannot decipher the user's message, they will be provided with the store's email, phone number, and hours to talk to a real employee.

## Table of contents

* [Setup](#setup)
  * [Windows](#windows-powershell)
  * [Unix](#unix-bash)
  * [Run Bot](#run)
* [Main Bot (input/output)](#main-bot)
* [Mini Bots (products & store information)](#product--store-mini-bots)
* [Tests](#tests)
  * [All cases](#test-all-cases)
  * [Selected cases](#test-selected-cases)
* [API](#api)
  * [Store Info API](#store-info-api)
  * [Product Info API](#product-info-api)
  * [Database API](#database-api)
* [New Features](#new-features)
  * [Nutrition Sub-Topic](#nutrition-sub-topic)
  * [5 Reasonable Responses](#5-reasonable-responses-outside-of-the-topic)
  * [Spelling Mistakes](#spelling-mistakes)

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

## Product & Store Mini-bots

This mini-bot will handle any question related to product price, stock, nutrition, and store information. The bot first determines what topic is of interest (product or store information) and breaks the user's message down into keywords. The bot then compares these words and checks them in order to create the most appropriate response, and returns the response to the main bot.

See in-depth documentation [here](app/products/README.md).

## Tests
We are using `pytest` for all of our tests. Our test cases can be found in the `test` folder.

### Test all cases:
```console
python -m pytest
```

### Test selected cases:

- database
- store_info
- prod_info
- intent_detection_test

```console
python -m pytest -v -m <selected case>
```

## API
You can call the API from any other Python script to check store's information or products information. This does not require the bot to be running or a diagflow key.

**Make sure to import the API correctly, as the API is not imported by default, and is dependent on your project's file hierarchy.**

### Store Info API

From this bot you can query the store's information.

`Example import for product info bot:`
```console
from app.products.store_info import StoreInfoHandler
```

`handle(string) -> string`
```console
StoreHandler = StoreInfoHandler()
message = "Where is the store?"
output = StoreHandler.handle(message)
# returns string: "It is 123 Main St"
```

`parse(string) -> object`
```console
StoreHandler = StoreInfoHandler()
message = "Where is the store?"
print(StoreHandler.parse(message))
# returns object: {'request': 'address'}
```

### Product Info API

From this bot you can query the store's products information.

`Example import for product info bot:`
```console
from app.products.product_info import ProductInfoHandler
```

`handle(string) -> string`
```console
StoreHandler = ProductInfoHandler()
message = "How much does a banana cost?"
output = StoreHandler.handle(message)
# returns string: "Bananas cost $0.67 per kg."
```

`parse(string) -> object`
```console
StoreHandler = ProductInfoHandler()
message = "How much does a banana cost?"
output = StoreHandler.parse(message)
# returns object: {'request': 'price', 'id': '4011'}
```

### Database API
The database API also allows queries straight from the database.

`Example import for database:`
```console
from app.database import Database
```

`Database lifecycle:`
```console
db = Database.instance()
db.connect()
db.init_database()
# queries or methods
db.close()
```

`get_product("id", str) -> List`
```
output = db.get_product("id", "4011")
# returns list: [OrderedDict([('id', '4011'), ('name', 'banana'), ('names', 'bananas'), ('price', 0.67), ('price_scale', 'per kg'), ('in_stock', True), ('calories', 89), ('protein', '1.1 g'), ('carbs', '22.8 g'), ('sugar', '12.2 g'), ('fat', '0.3 g')])]
```

## New Features

### Nutrition Sub-Topic

With nutrition sub-topic, the bot will also provide nutrition information for the product, which will help user decide whether to buy the product or not.

![nutrition-snippet](snippets/nutrition.png)

### 5 Reasonable responses outside of the topic

With 5 reasonable responses outside of the topic, the bot will provide a more fluent response to the user. This will help the user reword their question if the bot does not understand the question or variety in bot's responses, such as refund or replacement for the product, which allows for more smooth and realistic conversation.

![response-snippet](snippets/response.png)

### Spelling Mistakes

With spelling mistakes handled by Google's Diagflow API, the bot will provide a more accurate response to the user.

![correcttion-snippet](snippets/correction.png)

### Synonym Recognition

With synonym recognition handled by Google's Diagflow API, the bot will provide a more accurate response to the user.

![correcttion-snippet](snippets/synonym.png)

### Named Entity Recognition

With Named Entity Recognition handled by Google's Diagflow API, the bot will provide a more accurate response to the user.

![correcttion-snippet](snippets/entity.png)

### Sentiment Analysis

With Sentiment Analysis handled by Google's Diagflow API, the bot will provide a more accurate response to the user.

![correcttion-snippet](snippets/sentiment.png)