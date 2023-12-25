import random

print("Hey man, you just ran this program. Now I'm gonna generate a password for you.")

# The lowercase letters that we are gonna choose from
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# The uppercase letters that we are gonna choose from
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# The special characters we are gonna choose from
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', ';', ':', ',', '.', '<', '>', '/', '?']

random_character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', ';', ':', ',', '.', '<', '>', '/', '?']

character_one = str(random.randint(0, 9))
character_two = str(random.choice(lowercase_letters))
character_three = str(random.choice(uppercase_letters))
character_four = str(random.choice(special_characters))
character_five = str(random.choice(random_character))
character_six = str(random.choice(random_character))
character_seven = str(random.choice(random_character))
character_eight = str(random.choice(random_character))

password = [character_one, character_two, character_three, character_four, character_five, character_six, character_seven, character_eight]

random.shuffle(password)

# Join the password
password_str = ''
for char in password:
    password_str += char

print("Alright Bud, Your password is", password_str)
