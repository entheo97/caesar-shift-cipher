#!/usr/bin/env python3

def plaintext_message_encrypt(plaintext_message, key=3):
    """Encrypt plaintext using the Caesar Shift cipher algorithm."""
    ciphertext_string = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for plaintext_letter in plaintext_message:
        try:
            plaintext_letter_index = alphabet.index(plaintext_letter)
            ciphertext_index = plaintext_letter_index + key
            ciphertext_index = ciphertext_index % 26
            ciphertext_letter = alphabet[ciphertext_index]
            ciphertext_string += ciphertext_letter
        except ValueError:
            ciphertext_string += plaintext_letter
    print(ciphertext_string)