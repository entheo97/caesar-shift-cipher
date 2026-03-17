def caesar(cyphertext):
    """
    Brute forces a Caesar cipher by trying all 26 possible shift values.
    Prints each candidate plaintext for manual inspection.

    Args:
        cyphertext (str): The encrypted string to decode.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift_value = 0
    plaintext = []
    for shift_value in range(26):  # try all 26 possible shifts
        for character in list(cyphertext.lower()):
            if character not in alphabet:  # preserve spaces and punctuation
                plaintext.append(character)
                continue
            new_index = alphabet.index(character) + shift_value  # shift letter forward  
            new_index = new_index % 26  # wrap around if new index exceeds 25
            plaintext.append(alphabet[new_index])
        print(''.join(plaintext))  # print candidate plaintext for this shift
        plaintext = []  # reset for next shift

caesar('NZXMTYP AWLYPE VTEP ASZYP')
