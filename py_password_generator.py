import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the password Generator")

letters_needed = int(input("How many letters do you need in your password?\n"))
numbers_needed = int(input("How many letters do you need in your password?\n"))
symbols_needed = int(input("How many symbols do you need in your password?\n"))

list = []
chosen_letters = 0
chosen_numbers = 0
chosen_symbols = 0
# for letters
while (chosen_letters != letters_needed):
    letters_chosen = random.choice(letters)
    list.append(letters_chosen)
    chosen_letters += 1
# for symbols
while (chosen_numbers != numbers_needed):
    numbers_chosen = random.choice(numbers)
    list.append(numbers_chosen)
    chosen_numbers += 1
# for symbols

while (chosen_symbols != symbols_needed):
    symbols_chosen = random.choice(symbols)
    list.append(symbols_chosen)
    chosen_symbols += 1

random.shuffle(list)
encrypted_password = ""
for characters in list:
    encrypted_password += characters
print(f"Here is your password generated:{encrypted_password}")
