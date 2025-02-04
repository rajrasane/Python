# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

import random

def mult(a):
    res = a * random.randint(1,100)
    print(res)

mult(10)