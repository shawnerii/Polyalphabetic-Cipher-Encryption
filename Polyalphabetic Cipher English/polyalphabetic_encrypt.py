def encrypt_vigenere(plaintext, key):

    ciphertext = []
    key = key.upper()
    key_length = len(key)

    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(char)
    
    return ''.join(ciphertext)

if __name__ == "__main__":
    plaintext = input("Enter plaintext for testing encryption: ")
    key = input("Enter encryption key: ")
    ciphertext = encrypt_vigenere(plaintext, key)
    print("Ciphertext:", ciphertext)