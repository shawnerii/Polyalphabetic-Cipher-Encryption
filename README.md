in Monoalphabetic Cipher each letter in the text is mapped to a unique letter in the ciphertext using a fixed key. It is vulnerable to frequency analysis because the relative frequencies of letters are predictable.

The main steps are:

1. Generate a substitution key.

2. Implement the encryption and decryption functions.

3. Use frequency analysis as an analysis technique to break the cipher.

For the German text I specifically encrypted only the English alphabets so ä’, ‘ö’, ‘ü’, ‘ß would remain unchanged. In this case only the code for the attack is needed to be adjusted for the German letter frequencies.
