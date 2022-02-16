class Bot:

    def __init__(self):
        self.greeting()

    def greeting(self):
        print("Hi!")
        options = "Please choose from one of the following options:\n a)Store information\n b)Product information\n c)Other concerns"
        print(options)
        while(True):
            userInput = input().lower()
            if(userInput not in ["a","b","c","a)","b)","c)"]):
                print("Incorrect input! Please enter a,b or c: ")
            else:
                if(userInput == ["a","a)"]):
                    self.getStoreInfo()
                elif(userInput == ["c","c)"]):
                    self.getCustomerService()
                else:
                    self.getProductInfo()
               # print("Is there anything else I could help you with? (Yes/No)")
                #userInput = lower(str(input()))
                #if(userInput not in ["yes","no"]):
                  #  print()


    def getStoreInfo():
        print("store info")

    def getCustomerService():
        print("customer service info")
    
    def getProductInfo():
        print("product info")
