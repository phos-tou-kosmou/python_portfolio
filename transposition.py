#!/bin/python3
import numpy as np

Array = np.ndarray
x: Array = np.array([[1, 2, 3, 4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
y: Array = np.array([[1, 2, 3, 4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])

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
    length_y: int = len(y)

    if(length_x != length_y or len(x) != len(y)):
        return "Warning: You can only add matrices with corresponding dimensions (i.e. 2x2 + 2x2, 3x2 + 3x2)"
    
    newList: Array = np.arange(length_y*len(y))
    
    array_y_list: Array = create_list(y)
    array_x_list: Array = create_list(x)

    
    #TODO: Implement generator that allows me to add each index and abstract for multiplication
    for i, val in enumerate(array_y_list):
        newList[i] = val + array_x_list[i]
        
    thing: Array = newList.reshape(length_y, len(y))
    print(result)
    
    return result



def multiply_arrays(x: Array, y: Array) -> Array:
    length_x: int = len(x)
    length_y: int = len(y)

    newList: Array = np.arange(length_y*len(y))

    array_y_list: Array = create_list(y)
    array_x_list: Array = create_list(x)

    j: int = 0    
    
    #TODO: Implement second for loop, which traverses each column using modulus arithmetic and orbit groups
    for i, val in enumerate(array_y_list):
        newList[i] = val + array_x_list[j]
        j = (j+len(x)) % (len(x)*len(x))
        print(j)
        
    result: Array = newList.reshape(length_y, len(y))
    print(result)

    return result



def create_list(x: np.ndarray) -> list:
    list_of_array = [w for y in x for w in y]
    return list_of_array

def main(x: np.ndarray) -> np.ndarray:
    transpose(x)

multiply_arrays(x, y)
