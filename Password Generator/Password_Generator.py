import random

# Character pools for password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# This list will store all randomly chosen characters
password_list = []

# User input
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Add random letters
for number in range(nr_letters):
    password_list.append(random.choice(letters))
# Add random symbols
for number in range(nr_symbols):
    password_list.append(random.choice(symbols))
# Add random numbers
for number in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle to randomize order
random.shuffle(password_list)

# Convert list to string
password = ""
for i in password_list:
    password += i

print(f"Your password is: {password}")
