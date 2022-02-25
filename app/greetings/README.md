# Greetings and Routing part

## Implementation

We use Dialogflow agent to detect user's intent and respond accordingly. With the help of the API, the conversation is maintained in a more natural way and flexible with different user inputs. The agent is configured to respond to the following intents:

1. Greetings
2. Product information
3. Store information
4. Other concerns

## Usage

Currently, to use the bot, you need to contact us to get the API credentials. After having the credentials, you can use the bot by following the steps:

1. Install package `pip install google-cloud-dialogflow`
2. Set enviroment variables `GOOGLE_APPLICATION_CREDENTIALS` to the path of the API key in your device
3. Run the bot using the command `python main.py`