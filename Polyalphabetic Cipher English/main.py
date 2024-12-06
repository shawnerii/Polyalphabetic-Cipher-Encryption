from key_generation import generate_vigenere_key
from polyalphabetic_encrypt import encrypt_vigenere
from polyalphabetic_decrypt import decrypt_vigenere
from brute_force_vigenere import brute_force_vigenere

def main():
    key_length = int(input("Enter key length for generating a random key: "))
    key = generate_vigenere_key(key_length)
    print(f"Generated Key: {key}\n")

    plaintext = input("Enter plaintext for encryption: ")
    ciphertext = encrypt_vigenere(plaintext, key)
    print(f"Ciphertext: {ciphertext}\n")

    decrypted_text = decrypt_vigenere(ciphertext, key)
    print(f"Decrypted Text: {decrypted_text}\n")

    key, plaintext = brute_force_vigenere(ciphertext, key_length)
    if key:
        print("Successful Brute Force Attempt:")
        print(f"Key: {key}, Decrypted Text: {plaintext}")
    else:
        print("No valid decryption found using brute force.")

if __name__ == "__main__":
    main()