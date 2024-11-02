import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)


user_input = input("How many characters do you want in your password? ")


while True: 

    try:
        characters_number = int(user_input)
        if characters_number < 8:
            print("Your number should be at least 8.")
            user_input = input("Please enter your number again: ")
        else:
            break
    except:
            print("Please enter numbers only.")
            user_input = input("How many characters do you want in your password? ")

random.suffle(s1)
random.suffle(s2)
random.suffle(s3)
random.suffle(s4)

part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))

result = []

for x in range(part1)

