# -*- coding: utf-8 -*-

from itertools import starmap, cycle
import sys

def encrypt(message, key):
    message = filter(str.isalpha, message.upper())
    def enc(c,k):
        return chr(((ord(k) + ord(c) - 2*ord('A')) % 26) + ord('A'))
    return "".join(starmap(enc, zip(message, cycle(key))))

def decrypt(message, key):
    def dec(c,k):
        return chr(((ord(c) - ord(k) - 2*ord('A')) % 26) + ord('A'))
    return "".join(starmap(dec, zip(message, cycle(key))))

op = int(input("\n Vigenere \n\n [1] - Encrypt: \n [2] - Decrypt: \n>>"))

text = input("TEXT: ")
key = input("KEY: ")

encr = encrypt(text, key)
decr = decrypt(encr, key)

if op == 1:
    print ("\n\n"+encr)
elif op == 2:
    print ("\n\n"+decr)
else:
    sys.exit(0)