class Bot:

    def __init__(self):
        self.greeting()

    def greeting(self):
        print("Hi!")
        options = "Please choose from one of the following options:\n a)Store information\n b)Product information\n c)Other concerns\n d)Exit"
        while(True):
            print(options)
            userInput = input().lower()
            if(userInput not in ["a","b","c","d","a)","b)","c)","d)"]):
                print("Incorrect input! Please enter a,b or c: ")
            else:
                if(userInput in ["a","a)"]):
                    self.getStoreInfo()
                elif(userInput in ["b","b)"]):
                    self.getProductInfo()
                elif(userInput in ["c","c)"]):
                    self.getCustomerService()
                else:
                    print("Goodbye!")
                    break
                print("Is there anything else I could help you with?")



    def getStoreInfo(self):
        print("store info")

    def getCustomerService(self):
        print("customer service info")
    
    def getProductInfo(self):
        print("product info")
