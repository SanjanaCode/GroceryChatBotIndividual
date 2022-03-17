# Other Concerns

## Methods
The `OtherConcerns` class has three methods:

1. `handle()`:Is the principal methods which calls methods that handle returns and exchanges, any other questions that are not related to store or product information, or when the bot does not understand what the user types. It also analyzes the sentiment score from the dialogflow api and outputs a response according to whether the user's text denotes a positive or negative sentiment (sentiment classification).

2. `handleExchange()`:Provides response about how they can exchange products when user asks about exchange related concerns for products.

3. `handleRefunds()`:Provides response about how they can return and get a refund for products when user asks about refund related concerns for products.

## Implementation

Based on tone of the user text, the Bot will respond with a sentiment appropriate response (Based on whether the sentiment score is positive or negative) before providing a solution to the user's concerns.

If the intent detected is about exchanges: `handle()` calls `handleExchange()`

If the intent detected is about refunds: `handle()` calls `handleRefunds()`

To deal with any other questions that do not fall in the categories of product info, store info, exchanges or refunds, the chatbot provides 3 options:

1. First the chatbot asks if the user would like to visit the store. If user responds yes, the bot provides the store address.

2. If user responds no to the above question, then the bot asks if user would like to be contacted by a human agent. If user responds yes to this question, the bot collects the user's phone number and a brief description of their concern. The bot also informs the user that the human agent will get back to them within 24 hours.

3. Finally, if the user responds no to both of the above questions, then the bot provides the user with the customer service number so that the user can contact the customer service at their own convenience.
