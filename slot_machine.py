import random

def get_deposit():
    deposit=input("how much money would you like to deposit?")
    if deposit<="0":
        print ("zero or negative deposit not allowed")
    else:    
        print (f"your deposit of {deposit} amount successful")
    return deposit

def contd():
    cont=input("do u want to continue? y or n")
    return cont

def get_balance(amt,balance):
    balance=int(balance)+int(amt)
    print (f"the total balance is {balance}")
    return balance

if __name__ =="__main__":
    curr_bal=0
    prev_balance=0
    while True:
        prev_balance=curr_bal
        amt=get_deposit()
        curr_bal=get_balance(amt,curr_bal)
        print(f"Previous Balance: {prev_balance}")
        print(f"Current Balance: {curr_bal}")  
        # balance(amt,balance)  
        # print (f"total remaining balance is {total_balance}")    
        flag=contd()
        
    

        if flag=="n":
            break



        
