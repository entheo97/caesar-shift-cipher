import argparse

parser = argparse.ArgumentParser(description='Caesar cipher brute force decoder. Classical cryptography CLI tool written in Python.', epilog='Written by Nathan Frank')
parser.add_argument('ciphertext', help='your undecoded text string. strings may contain letters, non-letter characters and whitespace')
parser.add_argument('-l', '--longform', help='longform output displays all 26 candidate solutions', action='store_true')

cli_commands = parser.parse_args()
