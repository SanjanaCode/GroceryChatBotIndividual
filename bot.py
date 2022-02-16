class Bot:

    def __init__(self):
        greeting()

    def greeting():
        print("Hi!")
        options = "Please choose from one of the following options:\n a)Store information\n b)Product information\n c)Other concerns"
        print(options)
        while(true):
            userInput = lower(str(input()))
            if(userInput not in ["a","b","c","a)","b)","c)"]):
                print("Incorrect input! Please enter a,b or c: ")
            else:
                if(userInput == ["a","a)"]):
                    getStoreInfo()
                elif(userInput == ["c","c)"]):
                    getCustomerService()
                else:
                    getProductInfo()
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
