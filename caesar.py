def caesar(cyphertext):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift_value = 0
    plaintext = []
    for shift_value in range(26):
        for letter in list(cyphertext.lower()):
            new_index = alphabet.index(letter) + shift_value
            new_index = new_index % 26
            plaintext.append(alphabet[new_index])
        print(''.join(plaintext))
        plaintext = []

caesar('ZBNNLZADPUKLCLSVWDHZO')
