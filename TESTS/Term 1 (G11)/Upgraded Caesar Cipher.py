def double_caesar_encrypt(plaintext, key1, key2):  # encrypt function
    ciphertext = ""  # empty string where the ciphertext will be stored after encryption
    position = 0  # position of each letter starting from the first letter
    for letter in plaintext:
        char = letter
        if char.isalpha():  # Alphabetic check
            if position % 2 == 0:  # odd and even part
                shift = key1
            else:
                shift = key2
            if char.isupper():  # if the character is uppercase, do the following
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        else:
            encrypted_char = char  # characters that are not alphanumeric stay the same
        ciphertext += encrypted_char  # storing part
        position += 1  # Incremention
    return ciphertext

def double_caesar_decrypt(ciphertext, key1, key2):  # decrypt function
    decrypted_text = ""  # empty string where the decrypted text will be stored
    position = 0  # position of each letter starting from the first letter

    for letter in ciphertext:
        char = letter
        if char.isalpha():  # Alphabetic check
            if position % 2 == 0:  # odd and even part
                shift = key1
            else:
                shift = key2
            if char.isupper():  # if the character is uppercase, do the following
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
        else:
            decrypted_char = char  #characters that are not alphanumeric stay the same
        decrypted_text += decrypted_char  # storing part for decryption
        position += 1  #incremention
    return decrypted_text


def double_caesar_cipher():
    # menu script
    print("Caesar Cipher")
    print("This program will allow you to encrypt and decrypt messages TWICE")
    print("This is done so only the receiver gets the messages")
    print("This program can help protect all your messages from potential hackers trying to steal your data")
    print("The first shift key is applied to odd positions, while the second one is applied to even")
    print("Now please interact with the menu below so we can continue")
    while True:
        print("1. Encrypt a message using two distinct shift keys")
        print("2. Decrypt a message using two distinct shift keys")
        print("3. Quit the program")

        try:  # exception handling block here
            choice = int(input("Enter your choice (1/2/3): "))
        except ValueError:
            print("Invalid choice, please enter a valid number")
            continue

        if choice == 1:  # menu continuation
            plaintext = input("Enter the text to be encrypted: ")
            key1 = int(input("Enter the first shift key value (1-25): "))
            key2 = int(input("Enter the second shift key value (1-25): "))
            encrypted_text = double_caesar_encrypt(plaintext, key1, key2)
            print("Encrypted text:", encrypted_text)
        elif choice == 2:
            ciphertext = input("Enter the text to be decrypted: ")
            key1 = int(input("Enter the first shift key value (1-25): "))
            key2 = int(input("Enter the second shift key value (1-25): "))
            decrypted_text = double_caesar_decrypt(ciphertext, key1, key2)
            print("Decrypted text:", decrypted_text)
        elif choice == 3:
            break
        else:
            print("Sorry, The choice is invalid choice, please try again.")
            continue

# menu call
double_caesar_cipher()
