class OtherConcerns:
    #method:return response for other concerns
    def concernsHandler(self, userText):
        #Ask user if they would want to visit store
        print("Would you like to visit our store to resolve your concerns?")
        userInput = input().lower() 
        #if yes, give them store info.   
        if(userInput=='yes'):
            print("Here is our store address: Walmart\n 123 Main Street\n Toronto, Ontario\n M5V 2K7")

        #Else ask if they would like to be contacted by phone. Collect their phone number/email and a short description of concerns. If yes, store their info in database. If no, provide them with customer service contact number.
        else:
            print("Would you like us to contact you by phone?")
            userInput = input().lower() 
            if(userInput=='yes' or userInput=='sure'):
                print("Please give us your phone number and a brief desciption of your concerns. Our customer service agent will get back to you within 24 hours")
                userInput = input().lower()
                print("Awesome! We will get back to you soon.")
            #TO DO: parse userInput to obtain phone number and description of concern. Then,store in database.
            else:
                print("Here is our cutomer service number:416-555-1234\n You can also contact this number and our customer service agents will assist you.")
