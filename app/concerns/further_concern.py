class OtherConcerns:
    #method:return response for other concerns
    def concernsHandler(self):
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
            if(userInput=='yes'):
                print("Please give us your phone number for our agent to contact you:")
                phoneNum = input()
                #TO DO: Store phone number in database.
                print("Please give us a brief description of your concern:")
                descConcern = input()
                 #TO DO: Store customer concern in database.
                print("Our customer service agent will address your issue within 24 hours.")
            else:
                print("Here is our cutomer service number:416-555-1234\n You can contact this number and our customer service agents will assist you.")
        return None