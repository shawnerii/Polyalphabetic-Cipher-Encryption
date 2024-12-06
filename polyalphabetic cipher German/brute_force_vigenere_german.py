import itertools
import string
from collections import Counter
from polyalphabetic_decrypt_german import decrypt_vigenere

def word_frequency_check(text):
    common_words = ["DER", "DIE", "UND", "IN", "ZU", "MIT", "AUF", "IST", "DES", "SIE", "VON", "NICHT", "DAS"]
    words = text.upper().split()
    counter = Counter(words)

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