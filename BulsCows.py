# projekt_2.py: druhý projekt do Engeto Online Python Akademie
# 
# Autor: Martin Lampart
# email: westn.m01@gmail.com

# Popis: Hra Bulls & Cows
import random
separator = "-" * 50
def welcome():  
    print("Hello, welcome to the game Bulls and Cows!" )
    print(separator)
    print("I ve generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
    print(separator)

def generate_secret_number():
    number = random.sample(range(1, 9), 4)
    print(number)  
    return number

def get_bulls_and_cows(number, keys):
    bulls = 0
    cows = 0
          
    #pocitame byky
    for i in range(0, len(number)): # 
        if int(keys[i]) == number[i]:
            bulls += 1
           # konec počítání býku
    
    for i in range(len(keys)):
        if int(keys[i]) in number:
            cows += 1
    return bulls, cows
def play_bulls_and_cows():
    welcome()
    number = generate_secret_number()
    
    

    while True :
        keys = input(">>> ")

        if len(keys) < 4 or len(keys) > 4:
            print("Wrong number. Try again.")
            continue
        elif keys.isnumeric() == False:
            print("You did not enter the number. Try again.")
            continue
       
        elif len(number) != len(set(keys)):
            print("Number is duplicited. Try again.")
            continue
        else:
            bulls, cows = get_bulls_and_cows(number, keys)
            bull_word = "bull" if bulls == 1 else "bulls"
            cow_word = "cow" if cows == 1 else "cows"
            line = "-" * 50
            print(f"{bulls} {bull_word}, {cows} {cow_word}\n{line}")

        if bulls == 4:
            print("You won!")
            break
            
play_bulls_and_cows()



       


        

