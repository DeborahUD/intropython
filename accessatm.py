# declare a user dictionary that stores the pin and balance of the user
user={
    'pin': 2345,
    'balance': 1000
}

# defines the functions and variables
def withdraw_cash():
    while True:
        amount=int(input("Enter the amount you want to withdraw: "))
        if amount> user['balance']:
            print("Insufficient funds")
        else:
            user['balance']=user['balance']-amount
            print(f"{amount} successfully withdrawn")
            print('')
            print("Take your cash")
            return False
# defines the balance function
def balance_enquiry():
    print(f"Total balance {user['balance']} ")
    print('')
# this declares the isquit variable with the value as False
isQuit=False
print('')

# welcomes the user to the atm machine
print("Welcome to Access Bank")
pin=int(input("Please enter your four digit pin: "))
if pin==user['pin']:
    while isQuit==False:
        print("what do you want to do")
        print("Enter 1 to withdraw cash \n Enter 2 to check your balance \n Enter 3 to cancel")
        
        query=int(input("Enter the number corresponding to the activity you want to do: "))
        if query==1:
            withdraw_cash()
        elif query==2:
            balance_enquiry()
        elif query==3:
            isQuit=True
        else:
            print("select from the options shown")
else:
    print("Wrong pin")