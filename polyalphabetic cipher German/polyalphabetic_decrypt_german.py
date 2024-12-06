def decrypt_vigenere(ciphertext, key):
    plaintext = []
    key = key.upper()
    key_length = len(key)
    german_chars = 'ÄÖÜßäöü'

    for i, char in enumerate(ciphertext.upper()):
        if char in german_chars or not char.isalpha():
            plaintext.append(char)
        else:
            shift = ord(key[i % key_length]) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            plaintext.append(decrypted_char)

    return ''.join(plaintext)

if __name__ == "__main__":
    ciphertext = input("Enter ciphertext for testing decryption: ")
    key = input("Enter decryption key: ")
    plaintext = decrypt_vigenere(ciphertext, key)
    print("Decrypted Text:", plaintext)