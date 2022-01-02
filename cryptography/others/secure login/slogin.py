# -*- coding: utf-8 -*-

import hashlib
import os
import sys


def codSHA512(string):
    hs = hashlib.sha512(string.encode("UTF-8"))
    hs.update(string.encode("UTF-8"))
    hs = hs.hexdigest()
    return hs


def testSHA512(string, hs):
    if codSHA512(str(string)) == hs:
        print("\nAccess allowed")
        return True
    else:
        print("\nUnauthorized access")
        return False


def write(login, hash, salt):
    login = str(login)
    hash = codSHA512(str(hash) + str(salt))
    with open("database.txt", 'a', encoding='UTF-8') as arq:
        arq.write("\n" + login + "\n" + hash + "\n" + str(salt))
        arq.close()


def add():
    login = input("\nLogin: ")
    passwd = input("Password: ")
    salt = os.urandom(8)
    try:
        write(login, passwd, salt)
        print("\nLogged in access\n")
    except:
        print("\n;-; Error! try again \n")


def list():
    with open('database.txt', 'r') as f:
        database = f.readlines()
        for users in database:
            print(users)
        f.close()


def auth():
    login = input("\nLogin: ") + "\n"
    passwd = input("Password: ")
    with open("database.txt", 'r') as f:
        database = f.readlines()
        if login in database:
            posi = database.index(login)
            salt = database[int(posi) + 2]
            testSHA512(passwd + salt, database[int(posi) + 1].replace('\n', ''))
        else:
            print("\nUser does not exist\n")


def delete():
    user = input("\nLogin: ") + "\n"
    passwd = input("Password: ")
    with open("database.txt", 'r') as f:
        database = f.readlines()
        if user in database:
            posi = database.index(user)
            sal = database[int(posi) + 2]
            testSHA512(passwd + sal, database[int(posi) + 1].replace('\n', ''))
            database.pop(posi)
            database.pop(posi)
            database.pop(posi)
            f = open('database.txt', 'w')
            f.writelines(database)
            f.close()
            print("\nUser successfully removed\n")
        else:
            print("\nUser does not exist\n")


def menu():
    op = int(input(
        "\n[1] - New user:  \n[2] - Authenticate access: \n[3] - List users: \n[4] - Remove user: \n[5] - Quit: \n>> "))
    if op == 1:
        add()
    elif op == 2:
        auth()
    elif op == 3:
        list()
    elif op == 4:
        delete()
    else:
        sys.exit()


menu()
