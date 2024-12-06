DES encrypts data in 64 bit block using 56 bit key and performs a complex bitwise operation to
secure information. My code does the following:

• Generates a 56 bit encryption key.

• Defines the DES encryption and decryption functions using a standard DES
transformations.

• Encrypts and decrypts the text using DES, and storing results in text files.

My code is in separate Python files, each one is responsible for a specific part of the DES
algorithm. Which includes:

• key_schedule.py


• permutations.py

• sbox.py

• des_encrypt_decrypt.py

• utils.py

• main.py
