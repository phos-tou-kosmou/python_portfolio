#!/bin/python3
import numpy as np

Array = np.ndarray
x: Array = np.array([[1, 2, 3, 4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])

def transpose(x: np.ndarray) -> np.ndarray:
    length: int = len(x) 
    if(length == len(x[0])): 
        
        array_as_list: Array = create_list(x)
        
        newList: Array = np.arange(length*length)
        print(type(newList))
        k = 0

        for i, val in enumerate(array_as_list):
            if i == (length*length-1): break
            newList[k] = array_as_list[i]
            k = (k + length) % (length*length - 1)

        newList[len(newList)-1] = array_as_list[length*length-1]
        thing: Array = newList.reshape(length, length)
        print(thing) 

        return thing

def add_arrays(x: Array, y: Array) -> Array:
    length_x: int = len(x)
    length_y: int = len(x)

    if(length_x == length_y and len(x) == len(y)):
        transposey: Array = transpose(y)
        newList:    Array = np.arange(length_x*length_x)
        
        
        return 1

def create_list(x: np.ndarray) -> list:
    list_of_array = [w for y in x for w in y]
    return list_of_array

def main(x: np.ndarray) -> np.ndarray:
    transpose(x)

transpose(x)
