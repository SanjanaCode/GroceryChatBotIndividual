# Greetings and Routing part

## Implementation

We use Dialogflow agent to detect user's intent and respond accordingly. With the help of the API, the conversation is maintained in a more natural way and flexible with different user inputs. The agent is configured to respond to the following intents:

1. Greetings
2. Product information
3. Store information
4. Other concerns

### Methods

- `start_conversation`: runs an inifinite loop and prompts for user input. The input is then sent to `detect_intent_texts` to get the intents of types: `Default Welcome Intent`, `Default Fallback Intent`, `product-info`, `store-info`, `other-concerns` and `Done-conversation`. The intent is then passed to `route_to_handler`. The conversation is continued until the user says `bye`.

- `detect_intent_texts`: requests response from the Dialogflow API with user input passed from `start_conversation`.

- `route_to_handler`: with hashmap, the intent passed from `start_conversation` is mapped to the correct handler classes: `ProductInfo`, `StoreInfo`, `OtherConcerns`. The handler class is then called with the user input as an argument.

## Usage

Currently, to use the bot, you need to contact us to get the API credentials. After having the credentials, you can use the bot by following the steps:

1. Install package `pip install google-cloud-dialogflow`
2. Set enviroment variables `GOOGLE_APPLICATION_CREDENTIALS` to the path of the API key in your device:
Windows Power Shell: `$env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"`
Windows Command Prompt: `set GOOGLE_APPLICATION_CREDENTIALS=KEY_PATH`
Linux or MacOS: `export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"`
3. Run the bot using the command `python main.py`