# -*- coding: utf-8 -*-

import sys

def encode():
    for c in texto:
        c.lower()
        if ord(c) <= ord('z') - shift:
            print(chr(ord(c) + shift), end='')
        else:
            print(chr(ord('a') + shift - (ord('z') - ord(c)) - 1), end='')

def decode():
    for c in texto:
        c.lower()
        if ord('a') <= ord(c) - shift:
            print(chr(ord(c) - shift), end='')
        else:
            print(chr(ord('z') - shift + (ord(c) - ord('a')) + 1), end='')

op = int(input("\n\nCesar \n[1] - Encrypt:  \n[2] - Decrypt: \n\n>> "))

texto = input("TEXTO: ")
texto = str(texto)
shift = input("CHAVE: ")
shift = int(shift)

if op == 1:
    encode()
elif op == 2:
    decode()
else:
    sys.exit(0)