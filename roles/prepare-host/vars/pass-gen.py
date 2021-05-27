#!/usr/bin/python

import crypt
import random
import sys
import getpass

pwd = getpass.getpass()

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars = []

for i in range(16):
    chars.append(random.choice(ALPHABET))

salt = "".join(chars)

print crypt.crypt(pwd, salt)

