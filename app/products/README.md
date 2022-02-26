## Products and Store info
This mini-bot will handle any question related to product price, stock, and store information. The bot first determines what topic is of interest (product or store information) and breaks the user's message down into keywords. The bot then compares these words and checks them in order to create the most appropriate response, and returns the response to the main bot.

### Class StoreProductHandler
A class used to reperesent a mini-bot to handle product queries.
```console
className = StoreProductHandler(runtime_mode)
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
#### `handle`
The entry point of the mini-bot. Main bot will call this method to pass in the message to process.
```console
response = StoreProductHandler(runtime_mode).handle(message)
```
###### Parameters
message: str
The message that the user sends to the bot.
###### Returns
response: str
The response string to the request message.
#### parse_query
Method to parse the query and return a tuple of (topic_name, arguments for handler).
```console
name, kwargs = StoreProductHandler(runtime_mode).parse_query(message)
```
###### Parameters
message: str
The message that the user sends to the bot.
###### Returns
name, kwargs: tuple
The tuple consisting of the topic name and keyword arguments for handler.
#### `parse_product_info`
Indicates whether the request is related to product information, and then breaks down the message into its keywords.
```console
matched, name, prod_words = StoreProductHandler(runtime_mode).parse_product_info(message)
```
###### Parameters
message: str
The message that the user sends to the bot.
###### Returns
matched, "product_info", prod_words: tuple
The tuple consisting of whether the request relates to product info or not, the topic name, and a dictionary of the keywords.
#### `parse_store_info`
Indicates whether the request is related to store information, and then breaks down the message into its keywords.
```console
matched, name, store_words = StoreProductHandler(runtime_mode).parse_store_info(message)
```
###### Parameters
message: str
The message that the user sends to the bot.
###### Returns
matched, "store_info", store_words: tuple
The tuple consisting of whether the request relates to store info or not, the topic name, and a dictionary of the keywords.
#### `handle_product_info`
Uses the identified keywords to create the appropriate product response message for the user query.
```console
reply = StoreProductHandler(runtime_mode).handle_product_info(message=None, **kwargs)
```
###### Parameters
message: str (optional)
The message that the user sends to the bot.
kwargs: dictionary
The keyword arguments identified by parse_product_info.
###### Returns
reply: str
The proper response for the product information request.
#### `handle_store_info`
Uses the identified keywords to create the appropriate store response message for the user query.
```console
reply = StoreProductHandler(runtime_mode).handle_store_info(message=None, **kwargs)
```
###### Parameters
message: str (optional)
The message that the user sends to the bot.
kwargs: dictionary
The keyword arguments identified by parse_store_info.
###### Returns
reply: str
The proper response for the store information request.