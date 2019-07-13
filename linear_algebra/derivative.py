#!/bin/python3

def derivative(exponent, num):
    if num == 0 or num == 1: return 1
    
    if num > exponent: return 0
    elif num == exponent: return 1
    else: result = factorial(exponent, num)
    print("%dX^%d")%(result, exponent) 

def factorial(x, y):
    j = 1
    for i in range(0, y): 
         j *= x
         x = x - 1   
    return j

print(derivative(5, 3))
