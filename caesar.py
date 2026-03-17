def caesar(cyphertext):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift_value = 0
    plaintext = []
    for shift_value in range(26):
        for character in list(cyphertext.lower()):
            if character not in alphabet:
                plaintext.append(character)
                continue
            new_index = alphabet.index(character) + shift_value
            new_index = new_index % 26
            plaintext.append(alphabet[new_index])
        print(''.join(plaintext))
        plaintext = []

caesar('NZXMTYP AWLYPE VTEP ASZYP')
