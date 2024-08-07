import random
import sys

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
        exit_program()
    else:    
        print (f"your deposit of {deposit} amount successful")
    return deposit

def exit_program():
     sys.exit(0)


def contd():
    cont=input("do u want to continue? y or n")
    if cont=="n":
        exit_program()
              

def get_balance(amt,balance):
    balance=int(balance)+int(amt)
    return balance

def bet_win(win_lines,bet_amt):
    total_amt=int(win_lines)*int(bet_amt)
    return total_amt

def no_of_lines():
    line=input("enter how many lines you want to bet")
    if int(line)<=3 :
        line_amt=input("enter your bet amount per line")
        bet_amt=int(line)*int(line_amt)
        print (f"the total bet amount is {bet_amt}")
        return bet_amt
    else:
        print ("Lines should be numeric and less than 4")
        exit_program()
        
def place_bet(bet_amt,curr_balance):
    if int(curr_balance)>=int(bet_amt):
        print ("placing the bet now")
    else:
        print ("current balance is insuffecient")
        exit_program()
        
def rem_bal(total_won,curr_bal,bet_amt):
    if total_won==0:
        curr_bal=curr_bal-bet_amt
    else:
        curr_bal=curr_bal+ total_won
    return curr_bal

def display_lines():
       list(map(print,lines))


def clear_list(list):
    list.clear()

def display_balance(curr_bal,prev_balance):
        print(f"Current Balance: {curr_bal}") 
        print(f"Previous Balance: {prev_balance}")
 
def win_count(lines):
    win_ctr=0
    for i in range(1, 4):
            
            recent = win_lines(lines[i-1])
            win_ctr=win_ctr+recent
    return win_ctr

def game():
    curr_bal=0
    prev_balance=0
    while True:
        prev_balance=curr_bal
        amt=get_deposit()
        curr_bal=get_balance(amt,curr_bal)
        display_balance(curr_bal,prev_balance)
        bet_amt=no_of_lines()
        place_bet(bet_amt,amt)       
        generate_line(row_len,col_len)
        display_lines()
        win_ctr=win_count(lines)
        total_won=bet_win(win_ctr,bet_amt)
        print (f"you have won {win_ctr} lines in this bet. Total money earned {total_won}")
        curr_bal=rem_bal(total_won,curr_bal,bet_amt)
        print (f"remaining balance after round {curr_bal}")
        list(map(clear_list,lines))
        contd()

if __name__ =="__main__":
    game()        
    



        
