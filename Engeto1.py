TEXTS = [
'''Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater Genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

user_name = input("Login name: ")
pass_word = input("Your Password: ")
separater = "-" * 40

print(separater)

login = {
    "bob":"123",
    "ann":"pass123",
    "mike":"password123",
    "liz":"pass123"
}

if user_name not in login:
    print(f"{user_name} is not registred!!")
    exit()
if pass_word != login[user_name]:
    print(f"Wrong password!!")
    exit()
else:
    print(f"Welcome to the application, {user_name.title()}")

print(f"We have {len(TEXTS)} texts to be analyzed.")
print(separater)
choosen_text = 0
list_len = len(TEXTS)

user_input = input(f"Enter a number btw. 1 and {list_len} to select: ")
if user_input.isnumeric():
    user_input = int(user_input)

choice = int(user_input)
if choice <= list_len and choice > 0:
    choosen_text = TEXTS[choice - 1]
else:
    print(f"{choice} is not btw numbers 1 - {list_len}. Ending app.")
    exit()

splited_text = choosen_text.split()
splited_clear = [word.strip("_ - , ? ! .") for word in splited_text]
numbers_len = [len(word) for word in splited_clear]
title_case = [word for word in splited_clear if word.istitle()]
upper_case = [word for word in splited_clear if word.isupper() and word.isalpha()]
lower_case = [word for word in splited_clear if word.islower() and word.isalpha()]
numeric = [word for word in splited_clear if word.isnumeric()]
numeric_int = [int(number) for number in numeric]
print(separater)

print(f"There are {len(splited_text)} words in the selected text.")
print(f"There are {len(title_case)} titlecase words.")
print(f"There are {len(upper_case)} uppercase words.")
print(f"There are {len(lower_case)} lowercase words.")
print(f"There are {len(numeric)} numeric strings.")
print(f"The sum of all the numbers {sum(numeric_int)}.")
print(separater)

print(f" LEN|  OCCURENCES    |NR.")
print(separater)
star = "*"
space = " "

unique_lengths = sorted(set(numbers_len))
for length in unique_lengths:
    count = numbers_len.count(length)
    print(f"{str(length).rjust(4)}| {star * (count)} {(space).ljust(13-count)} |{count}")
    