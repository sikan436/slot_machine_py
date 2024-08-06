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
    bal=0
    prev_balance=0
    while True:
        
        amt=get_deposit()
        balance=get_balance(amt,bal)
        prev_balance=balance+prev_balance
        # balance(amt,balance)  
        # print (f"total remaining balance is {total_balance}")    
        flag=contd()
        
    

        if flag=="n":
            break



        
