#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = str(number)[-1]
last_digit1 = int(last_digit)


if (last_digit1 > 5 and number > 0):
    print(f'Last digit of {number} is {last_digit1} and is greater than 5')
elif (last_digit1 == 0 and number == 0):
    print(f'Last digit of {number} is {last_digit1} and is 0')
else:
    print(f'Last digit of {number} is {last_digit1} and is less than 6 and not 0')
