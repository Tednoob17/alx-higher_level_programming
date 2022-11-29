#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number % 10)

if (number < 0):
    digit = -digit

if (digit > 5):
    print(f"last digits of {number:d} is {digit} and is greater than 5")
elif (digit == 0):
    print(f"last digits of {number:d} is {digit} and is 0")
else:
    print(f"last digits of {number:d} is {digit} and is less than 6 and not 0")
