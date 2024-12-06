import itertools
import string
from collections import Counter

def decrypt_vigenere(ciphertext, key):
    plaintext = []
    key = key.upper()
    key_length = len(key)

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            plaintext.append(decrypted_char)
        else:
            plaintext.append(char)

    return ''.join(plaintext)

def word_frequency_check(text):
    common_words = {'an', 'on', 'of', 'to', 'or', 'by', 'the', 'but', 'and'}
    words = text.lower().split()
    counter = Counter(words)

    one_letter_words = [word for word in words if len(word) == 1]
    if any(word not in {'i', 'a'} for word in one_letter_words):
        return False

    common_word_count = sum(counter[word] for word in common_words)
    return common_word_count > 8

def brute_force_vigenere(ciphertext, key_length):
    for key_tuple in itertools.product(string.ascii_uppercase, repeat=key_length):
        key = ''.join(key_tuple)
        decrypted_text = decrypt_vigenere(ciphertext, key)
        if word_frequency_check(decrypted_text):
            return key, decrypted_text
    return None, "No valid decryption found."

if __name__ == "__main__":
    ciphertext = input("Enter ciphertext for brute-force hacking: ")
    key_length = int(input("Enter assumed key length: "))
    key, plaintext = brute_force_vigenere(ciphertext, key_length)
    if key:
        print(f"Key: {key}, Decrypted Text: {plaintext}")
    else:
        print("No valid decryption found.")