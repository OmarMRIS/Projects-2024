from spellchecker import SpellChecker

def double_caesar_decrypt(ciphertext, key1, key2):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - key2) % 26 + 26 - key1) % 26 + ord('A'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - key2) % 26 + 26 - key1) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text

def interactive_double_caesar_bruteforce(ciphertext):
    spell = SpellChecker(language='en')
    most_meaningful_decrypted_text = ciphertext
    meaningful_word_count_of_most_meaningful_text = 0

    for key1 in range(1, 26):
        for key2 in range(1, 26):
            decrypted_text = double_caesar_decrypt(ciphertext, key1, key2)
            meaningful_word_count = 0
            words = decrypted_text.split(' ')

            for word in words:
                word = word.lower()
                if word in spell:
                    meaningful_word_count += 1

            if meaningful_word_count > meaningful_word_count_of_most_meaningful_text:
                meaningful_word_count_of_most_meaningful_text = meaningful_word_count
                most_meaningful_decrypted_text = decrypted_text

    print("Decrypted Text:")
    print(most_meaningful_decrypted_text)

print("Double Caesar Cipher Brute Force Decryption")
ciphertext = input("Enter the encrypted text: ")
interactive_double_caesar_bruteforce(ciphertext)
