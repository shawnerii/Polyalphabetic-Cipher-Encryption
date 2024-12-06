def encrypt_vigenere(plaintext, key):
    
    ciphertext = []
    key = key.upper()
    key_length = len(key)
    german_chars = 'ÄÖÜßäöü'

    for i, char in enumerate(plaintext.upper()):
        if char in german_chars or not char.isalpha():
            ciphertext.append(char)
        else:
            shift = ord(key[i % key_length]) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext.append(encrypted_char)

    return ''.join(ciphertext)

if __name__ == "__main__":
    plaintext = input("Enter plaintext for testing encryption: ")
    key = input("Enter encryption key: ")
    ciphertext = encrypt_vigenere(plaintext, key)
    print("Ciphertext:", ciphertext)