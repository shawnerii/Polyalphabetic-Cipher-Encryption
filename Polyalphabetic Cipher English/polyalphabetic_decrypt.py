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

if __name__ == "__main__":
    ciphertext = input("Enter ciphertext for testing decryption: ")
    key = input("Enter decryption key: ")
    plaintext = decrypt_vigenere(ciphertext, key)
    print("Decrypted Text:", plaintext)