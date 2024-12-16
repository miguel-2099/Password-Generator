import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

# Ask user for input and ensure it's a valid number
while True: 
    user_input = input("How many characters do you want in your password? ")

    try:
        characters_number = int(user_input)
        if characters_number < 8:
            print("Your number should be at least 8.")
        else:
            break
    except ValueError:
        print("Please enter numbers only.")

# Shuffle the lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

# Calculate parts of the password
part1 = round(characters_number * (30 / 100))  # Lowercase letters
part2 = round(characters_number * (20 / 100))  # Uppercase letters
part3 = round(characters_number * (20 / 100))  # Digits
part4 = characters_number - (part1 + part2 + part3)  # Special characters (the rest)

result = []

# Generate the password by adding random characters from each list
result += random.sample(s1, part1)  # Add lowercase letters
result += random.sample(s2, part2)  # Add uppercase letters
result += random.sample(s3, part3)  # Add digits
result += random.sample(s4, part4)  # Add punctuation

# Shuffle the result to make the password more random
random.shuffle(result)

# Join the list into a string and print the final password
password = ''.join(result)
print("Your generated password is:", password)
