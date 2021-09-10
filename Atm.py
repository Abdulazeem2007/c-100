class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber= cardnumber
        self.pin = pin

    def balanceInquiry(self):
        print("Your balance is $100")

    def cashWithdrawl(self,amount):
        new_amount = 100 -amount
        print("You withdrawed " + str(amount)+ " Your remaining balance is : " + str(new_amount))

def main():
    name = input("Hello What is your name?")
    print("Hello " + name)
    cardnumber = int(input("Insert your card number: "))
    if (cardnumber == 16):
        print("Proceed!")       
    elif cardnumber < 16:
        print("Proceed!")
    else:
        print("Proceed!")
    
    pin = int(input("Enter your pin: "))
    if (pin == 4):
       print("Proceed!")
    elif pin > 4:
        print("Proceed!")
    else:
        print("Proceed!")
    
    new_user = Atm(cardnumber, pin)

    print("Choose your activity")
    print("1. Balance Inquiry")
    print("2. Cash Withdrawl")
    activity = int(input("Enter activity choice: "))

    if (activity == 1):
            new_user.balanceInquiry()
        
    elif(activity == 2):
            amount = int(input("Enter the Amount: "))
            new_user.cashWithdrawl(amount)
    else:
            print("Enter a Valid Number")

if __name__ == "__main__":
    main()
        
    

    
    
