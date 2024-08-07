import random

row_len=3
col_len=3

slot_cards={
    "A":1,
    "B":2,
    "C":3,
    "D":4,
    "E":5
}
line1=[]
line2=[]
line3=[]
lines = [line1, line2, line3]

def generate_line(row_len,col_len):
    for i in range(row_len):
        for k in  range(col_len):
            if i==0:
                card=get_symb(slot_cards)
                line1.append(card)
            if i==1:
                card=get_symb(slot_cards)
                line2.append(card)
            if i==2:
                card=get_symb(slot_cards)
                line3.append(card)
                
  

def get_symb(symbol):
    all_symbol=[]
    for symbol,ind in symbol.items():
        all_symbol.append(symbol)
    rand_symb=random.choice(all_symbol)
    return rand_symb

def win_lines(line):

    cnt=line.count(line[0])

    if cnt!=3:

        return 0
    else:

        return 1
            

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

def no_of_lines():
    line=input("enter how many lines you want to bet")
    if int(line)<3:
        line_amt=input("enter your bet amount per line")
        bet_amt=int(line)*int(line_amt)
        print (f"the total bet amount is {bet_amt}")
        return bet_amt
    else:
        print ("line should be less than 3")
        
def place_bet(bet_amt,curr_balance):
    if int(curr_balance)>int(bet_amt):
        remaining_balance=curr_balance-bet_amt
        print (f"remaining balance: {remaining_balance}")
        return remaining_balance
    print("exiting from place_bet")

if __name__ =="__main__":
    curr_bal=0
    prev_balance=0
    while True:
        prev_balance=curr_bal
        amt=get_deposit()
        curr_bal=get_balance(amt,curr_bal)
        print(f"Previous Balance: {prev_balance}")
        print(f"Current Balance: {curr_bal}")  
        bet_amt=no_of_lines()
        place_bet(bet_amt,curr_bal)
        
        generate_line(row_len,col_len)
        print (line1)
        print (line2)
        print (line3) 
        print ("###################")
        win_ctr=0
        for i in range(1, 4):
            
            recent = win_lines(lines[i-1])
            win_ctr=win_ctr+recent
        print (f"you have won {win_ctr} lines in this bet")

        # for i in range(1,4):
        #     win_ctr=0
        #     recent=win_lines(line1
        #     win_ctr=win_ctr+recent
        #     print (f"total win lines till now {win_ctr}")
        line1.clear()
        line2.clear()
        line3.clear()



        
                
        # balance(amt,balance)  
        # print (f"total remaining balance is {total_balance}")    
        flag=contd()
        
    

        if flag=="n":
            break



        
