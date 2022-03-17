class OtherConcerns:
    
    def handle(self, sentimentNum, intent): 
        """
        Handles responses for other concerns such as refunds, exchanges and anything that the bot does not understand.
        parameters: 
                    sentimentNum - denotes whether the text from customer is a positive or negative sentiment.
                    intent - holds a string representing the intent detected.
        returns: nothing
        """
        # If sentimentNum is a negative number then the text denotes a negative sentiment. 
        # If sentimentNum is a positive number then the text denotes a positive sentiment.
        # If sentimentNum is equal to zero, it's a neutral sentiment so print nothing.
        if(sentimentNum<0):     
            print("We're sorry to hear that!")
        if(sentimentNum>0):
            print("That's great! Thank you for your feedback!")
        
        #If customer is asking for an exchange, direct it to the handleExchange() method.
        if(intent=="exchange-request"):
            self.handleExchange()
        #Else if customer is asking for a refund, direct it to the handleRefunds() method.  
        elif(intent=="refund-request"):
            self.handleRefunds()
        #For any other concerns or when the bot is unable to understand what the customer is saying:

        else:
            #Ask user if they would want to visit store
            print("Bot: Would you like to visit our store to resolve your concerns?")
            userInput = input("You: ").lower() 
            #if yes, give them store info.   
            if(userInput=='yes'):
                print("Bot: Here is our store address: Walmart\n 123 Main Street\n Toronto, Ontario\n M5V 2K7.")

            #Else ask if they would like to be contacted by phone. Collect their phone number/email and a short description of concerns. If yes, store their info in database. If no, provide them with customer service contact number.
            else:
                print("Bot: Would you like us to contact you by phone?")
                userInput = input("You: ").lower() 
                if(userInput == 'yes'):
                    print("Bot: Please give us your phone number for our agent to contact you.")
                    phoneNum = input("You: ")
                    #TO DO: Store phone number in database.
                    print("Bot: Please give us a brief description of your concern")
                    descConcern = input("You: ")
                    #TO DO: Store customer concern in database.
                    print("Bot: Our customer service agent will address your issue within 24 hours.")
                else:
                    print("Bot: Here is our customer service number:416-555-1234\n You can contact this number and our customer service agents will assist you.")

    def handleExchange(self):
        """
        Handles requests for exchanges
        parameters: nothing
        returns: nothing
        """
        print("Bot: You can exchange the product within 2 weeks (if perishable, then within 1-2 days) of purchase by visiting our store.\n Please ensure that: \n1. the product is unused \n2. the price tags are intact \n3. you bring the bill along with the product.")


    def handleRefunds(self):
        """
        Handles requests for refunds
        parameters: nothing
        returns: nothing
        """
        print("Bot: You can request for a refund or return in 2 ways:  1. place a request on our website(our agent will come to pick up the product) \n 2. directly visit our store\n Note that all requests for refunds or returns have to be made within 2 weeks of purchasing.\n After your refund/return is processed, the money will be refunded \n 1. To your original payment method (if paid by credit/debit card\n 2. As store credit")
