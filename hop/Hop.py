#!/usr/bin/env python
# coding: utf-8

# In[ ]:

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


number = 1
computerTurn = False
while True:
    if computerTurn:
        result = str(number)
        if number % 5 == 0:
            result = str('hope :)')
        print("my number: " + result)

    else:
        userNumber = input('ur turn: ')
        if (number % 5 == 0 and userNumber != 'hop') or (is_integer(userNumber) and number != int(userNumber)):
            print('wrong number, try again')
            continue

    number += 1
    computerTurn = not computerTurn
