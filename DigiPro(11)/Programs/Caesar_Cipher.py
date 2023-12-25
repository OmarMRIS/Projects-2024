import re

from spellchecker import SpellChecker

def encrypt(plaintext, key) : 
    ciphertext = ''
    for char in plaintext: 
        if char.isalpha() or char.isdigit(): 
            # get the ASCII value of the character 
            ascii_val = ord(char) 
            if char.isalpha(): 
                # shift the ASCII value by the key 
                shifted_val = ascii_val + key 
                # if the shifted value is out of the range of uppercase/ lowercase letters, wrap it around 
                if char.isupper(): 
                    if shifted_val > ord('Z'): 
                        shifted_val = ord('A') + ((shifted_val - ord('A')) % 26)
                else: 
                    if shifted_val > ord('z'): 
                        shifted_val = ord('a') + ((shifted_val - ord('a')) % 26)
                # convert the shifted ASCII value back to a character and add to the ciphertext 
                ciphertext += chr(shifted_val) 
            else: 
                # shift the digit by the key, and wrap around if necessary 
                shifted_val = (int(char) + key) % 10 
                ciphertext += str(shifted_val) 
        else:
            ciphertext += char
    return ciphertext 
    
def decrypt(ciphertext, key) : 
    plaintext = ""
    for char in ciphertext: 
        if char.isalpha(): 
        # handle uppercase and Lowercase Letters separately 
            if char. isupper(): 
                plaintext += chr((ord(char) - ord('A') - key) % 26 + ord('A')) 
            else:
                plaintext += chr((ord(char) - ord('a') - key) % 26 + ord('a')) 
        elif char.isdigit():
            plaintext += chr((ord(char) - ord('0') - key) % 10 + ord('0')) 
        else: 
            #Leave non-alphanumeric characters as they are 
            plaintext += char
    return plaintext

def extract_letters(word): 
    letters_only = re.sub("[^a-zA-Z]", "", word)
    return letters_only 

def brute_force_attack(encrypted_text): 
    decrypted_texts = []
    for shift in range(1, 26): 
        decrypted_text = decrypt(encrypted_text, shift) 
        decrypted_texts. append ( decrypted_text ) 
    
    # use a speLL checker to determine the most meaningful decrypted text 
    spell = SpellChecker(language = 'en')
    most_meaningful_decrypted_text = encrypted_text
    meaningful_word_count_of_most_meaningful_text = 0
    for decrypted_text in decrypted_texts:
        meaningful_word_count = 0
        words = decrypted_text.split(' ')
        for word in words:
            word = word.lower()
            word = extract_letters(word)
            if word in SpellChecker(language = 'en'):
                meaningful_word_count += 1
        if meaningful_word_count > meaningful_word_count_of_most_meaningful_text:
            meaningful_word_count_of_most_meaningful_text = meaningful_word_count
            most_meaningful_decrypted_text = decrypted_text
    return most_meaningful_decrypted_text

def menu():
    while True:
        print("Caeser Cipher")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Brute Force Attack")
        print("4. Quit")

        try:
            choice = int(input("Enter your choice (1/2/3/4):"))
        except:
            print("Invalid choice, please enter a valid number")
            continue
        if choice == 1:
            plainText = input("Enter the text to be encrypted: ")
            key = int(input("Enter the shift value (1-25): "))
            encryptedText = encrypt(plainText, key)
            print(encryptedText)
        elif choice == 2:
            cipherText = input("Enter the text to be decrypted: ")
            key = int(input("Enter the shift value (1-25): "))
            print(decrypt(cipherText, key))
        elif choice == 3:
            encryptedText = input("Enter text: ")
            print(brute_force_attack(encryptedText))
        elif choice == 4:
            break
        else:
            print("Invalid choice, try again")
            continue
menu()