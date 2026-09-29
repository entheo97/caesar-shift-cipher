#!/usr/bin/env python3

def plaintext_message_encrypt(plaintext_message, key):
    """Encrypts plaintext using the Caesar Shift cipher algorithm."""
    ciphertext_string = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for plaintext_letter in plaintext_message.lower():
        try:
            plaintext_letter_index = alphabet.index(plaintext_letter)
            ciphertext_index = plaintext_letter_index + key
            ciphertext_index = ciphertext_index % 26
            ciphertext_letter = alphabet[ciphertext_index]
            ciphertext_string += ciphertext_letter
        except ValueError:
            ciphertext_string += plaintext_letter
    print(f"Ciphertext: {ciphertext_string}\n")

def ciphertext_decrypt(ciphertext):
    """Decrypts ciphertext using the Caesar Shift cipher algorithm."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shift_value = 0
    plaintext = []
    # try all 26 possible shifts
    for shift_value in range(26):
        for character in list(ciphertext.lower()):
            if character not in alphabet:
                plaintext.append(character)
                continue
            new_index = alphabet.index(character) - shift_value  # shift letters backward
            new_index = new_index % 26  # wrap around if new index exceeds 25
            plaintext.append(alphabet[new_index])
        # print candidate plaintext for this shift
        print(f"Shift Value {shift_value:2d}: " + "".join(plaintext))
        plaintext = []  # reset for next shift

def main():
    while True:
        user_input = input("Enter 1 to encrypt\nEnter 2 to decrypt\nEnter 3 to quit\n")
        try:
            choice = int(user_input)
        except ValueError:
            print("Invalid entry. Please try again.\n")
            continue
        if choice == 1:
            plaintext_message = input("Enter plaintext message to encrypt: ")
            try:
                key = int(input("Enter a shift value between 1 and 25: "))
            except ValueError:
                print("Shift value must be a whole number\n")
                continue
            if not 1 <= key <= 25:
                print("Shift value must be between 1 and 25.\n")
                continue
            plaintext_message_encrypt(plaintext_message, key)
        elif choice == 2:
            ciphertext = input("Enter ciphertext message to decrypt for manual inspection: ")
            ciphertext_decrypt(ciphertext)
        elif choice == 3:
            quit()
        else:
            print("Invalid entry. Please try again.\n")
            main()

if __name__ == "__main__":
    main()