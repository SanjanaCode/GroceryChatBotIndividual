## Products and Store info
This mini-bot will handle any question related to product price, stock, and store information. The bot first determines what topic is of interest (product or store information) and breaks the user's message down into keywords. The bot then compares these words and checks them in order to create the most appropriate response, and returns the response to the main bot.

-------------------------
-------------------------

### SuperClass BaseHandler
A superclass used to reperesent skeleton for a mini-bot to handle product/store queries.
```console
className = BaseHandler()
```
###### Attributes:
runtime_mode: str
The environment that the bot is running in (i.e. DEV or PRODUCTION).
handler_map: dict
The mapping from sub-topic and corresponding handler.

-------------------------
### Methods
#### `__init__`
Construct all the necessary attributes for the ProductHandler object.
###### Parameters
None
###### Returns
None

#### `dispose` (common method)
This method releases any resources with this minibot (i.e. database connection).
```console
BaseHandler().dispose()
```
###### Parameters
None
###### Returns
None
#### `handle` (abstract)
The entry point of the mini-bot. Main bot will call this method to pass in the message to process.
```console
response = BaseHandler().handle(message)
```
###### Parameters
message: str
The message that the user sends to the bot.
###### Returns
response: str
The response string to the request message.

#### `parse` (abstract)
The entry point of the mini-bot. Main bot will call this method to pass in the message to process.
```console
response = BaseHandler().handle(message)
```
###### Parameters
message: str
The message that the user sends to the bot.
###### Returns
response: str
The response string to the request message.

-------------------------
-------------------------
### Class StoreInfoHandler
A class used to reperesent a mini-bot to handle store queries. Extension of BaseHandler.
```console
className = StoreInfoHandler()
```
###### Attributes:
runtime_mode: str
The environment that the bot is running in (i.e. DEV or PRODUCTION).
handler_map: dict
The mapping from sub-topic and corresponding handler.

-------------------------
### Methods
#### `__init__`
Construct all the necessary attributes for the ProductHandler object.
###### Parameters
None
###### Returns
None
###### Parameters
message: str
The message that the user sends to the bot.
###### Returns
matched, "store_info", store_words: tuple
The tuple consisting of whether the request relates to store info or not, the topic name, and a dictionary of the keywords.
#### `dispose` (common method)
This method releases any resources with this minibot (i.e. database connection).
```console
StoreInfoHandler().dispose()
```
###### Parameters
None
###### Returns
None
#### `handle` (override)
The entry point of the mini-bot. Main bot will call this method to pass in the message to process.
```console
response = StoreInfoHandler().handle(message)
```
###### Parameters
message: str
The message that the user sends to the bot.
###### Returns
response: str
The response string to the request message.
#### `parse` (override)
Indicates whether the request is related to store information, and then breaks down the message into its keywords.
```console
store_words = StoreInfoHandler().parse(message)
```
###### Parameters
message: str
The message that the user sends to the bot.
###### Returns
store_words: dictionary
A dictionary of the keywords for request to call thee handler.
#### `handle_store_info`
Uses the identified keywords to create the appropriate store response message for the user query.
```console
reply = StoreInfoHandler().handle_store_info(message=None, **kwargs)
```
###### Parameters
message: str (optional)
The message that the user sends to the bot.
kwargs: dictionary
The keyword arguments identified by parse_store_info.
###### Returns
reply: str
The proper response for the store information request.

-------------------------
-------------------------

### Class ProductInfoHandler
A class used to reperesent a mini-bot to handle product queries. Extension of BaseHandler.
```console
className = ProductInfoHandler()
```
###### Attributes:
runtime_mode: str
The environment that the bot is running in (i.e. DEV or PRODUCTION).
handler_map: dict
The mapping from sub-topic and corresponding handler.

-------------------------
### Methods
#### `__init__`
Construct all the necessary attributes for the ProductHandler object.
###### Parameters
None
###### Returns
None
#### `dispose` (common method)
This method releases any resources with this minibot (i.e. database connection).
```console
BaseHandler().dispose()
```
###### Parameters
None
###### Returns
None
#### `handle` (override)
The entry point of the mini-bot. Main bot will call this method to pass in the message to process.
```console
response = ProductInfoHandler().handle(message)
```
###### Parameters
message: str
The message that the user sends to the bot.
###### Returns
response: str
The response string to the request message.
#### `parse` (override)
Indicates whether the request is related to product information, and then breaks down the message into its keywords.
```console
prod_words = ProductInfoHandler().parse(message)
```
###### Parameters
message: str
The message that the user sends to the bot.
###### Returns
prod_words: dictionary
A dictionary of the keywords and id of products for request to call thee handler.
#### `handle_product_info`
Uses the identified keywords to create the appropriate product response message for the user query.
```console
reply = ProductInfoHandler().handle_product_info(message=None, **kwargs)
```
###### Parameters
message: str (optional)
The message that the user sends to the bot.
kwargs: dictionary
The keyword arguments identified by parse_product_info.
###### Returns
reply: str
The proper response for the product information request.