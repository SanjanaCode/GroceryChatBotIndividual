# grocery-chat-bot

###### An assistant chatbot for a grocery store that helps answer customer queries.

The chatbot will greet the user, then answer their question about store/product information other, more complex concerns.

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
  * [Store Info Bot API](#store-info-bot-api)
  * [Product Info Bot API](#product-info-bot-api)
  * [Database API](#database-api)

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

This mini-bot will handle any question related to product price, stock, and store information. The bot first determines what topic is of interest (product or store information) and breaks the user's message down into keywords. The bot then compares these words and checks them in order to create the most appropriate response, and returns the response to the main bot.

See in-depth documentation [here](app/products/README.md).

## Tests
We are using pytest for all of our tests. Our test cases can be found in the `test` folder.

### Test all cases:
```console
python -m pytest
```

### Test selected cases:

- database
- store_info
- prod_info
- intentDetectionTest

```console
python -m pytest -v -m <selected case>
```

## API
You can call the API from any other Python script to check store's information or products information. This does not require the bot to be running or a diagflow key.

**Make sure to import the correctly, as the API is not imported by default, and is dependent on your project's file hierarchy.**

### Store Info Bot API

From this bot you can query the store's information.

`Example import for product info bot:`
```console
from app.products.store_info import StoreInfoHandler
from app.products.database import STORE_INFO
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

### Product Info Bot API

From this bot you can query the store's products information.

`Example import for product info bot:`
```console
from app.products.product_info import ProductInfoHandler
from app.products.database import STORE_INFO
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
The database api also allows queries straight from the database.

`Example import for database:`
```console
from app.products.database import SQLiteDatabase, DatabaseType
```

`Database lifecycle:`
```console
db = SQLiteDatabase(DatabaseType.MEMORY)
db.connect()
db.init_database()
# queries or methods
db.close()
```

`get_product("id", int) -> List`
```
output = db.get_product("id", "4011")
# returns list: [OrderedDict([('id', '4011'), ('name', 'banana'), ('names', 'bananas'), ('price', 0.67), ('price_scale', 'per kg'), ('in_stock', True)])]
```

`execute_query(string) -> database cursor`
```
output = db.execute_query("SELECT * FROM product;")
#returns cursor: <sqlite3.Cursor object at 0x000001CB91165810>
```
To get the data from the cursor, use this custom function (can be modified):
```console
def query_result_to_str(cursor):
        result = []
        for row in cursor:
            row_data = []
            for attr in row:
                row_data.append(str(attr))

            # Convert last attr
            row_data[-1] = "1" if row_data[-1] else "0"
            result.append(",".join(row_data))

        return "\n".join(result).
```

Example case:

```console
output = query_result_to_str(db.execute_query("SELECT * FROM product;"))
# returns string: "4011,banana,bananas,0.67,per kg,1
# 3022,strawberry,strawberries,3.99,per box,1
# 2011,apple,apples,0.49,per kg,1
# 5044,pear,pears,0.87,per kg,1
# 8088,bread,bread,2.99,per loaf,1"
# Each product has a unique id, name, names, price, price_scale, and in_stock.
```
