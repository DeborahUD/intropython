
users=[
    {"pin":1234, "balance":1000},
    {"pin":2345, "balance":2000},
    {"pin":3456, "balance":3000}

]
user1=users[0]
user2=users[1]
user3=users[2]
count=0
action=False

def withdrawCash():
    amount=int(input('Enter the amount you want to withdraw'))
    if amount> user1['balance']:
        print('Insufficient funds')
    else:
        user1['balance']=user1['balance']-amount
        print("Take your cash")

def balanceEnquiry():
    pin=int(input("Enter your pin: "))
    for pin in users:
        if pin==user1['pin']:
            print(f"Total balance {user1['balance']} ")
        elif pin==user2['pin']:
            print(f"Total balance {user2['balance']}")
        elif pin==user3['pin']:
            print(f"Total balance {user3['balance']}")

print('')
    


print('Welcome to UBA bank')
pin=int(input("Enter your 4 digit pin: "))

for pin in range(len(users)):
    
    # if pin in users['pin']:
    
        print('Enter 1 for withdrawal \n Enter 2 to check balance \n Enter 3 to cancel')
        action=int(input("Enter your transaction: "))

        if action==1:
            withdrawCash()
        if action==2:
            balanceEnquiry()
        if action==3:
            cancel=True
        else:
            print('Choose options 1,2,3')
    # else:
    #     print('wrong Pin')
    
    # been able to allow all users with different pins access the atm but ive not been able to differentiate the account.

