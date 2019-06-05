#!/bin/python3
import numpy as np
from multiprocessing import Pool

x = np.array([[1, 2, 3, 4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
y = np.array([[1, 2, 3, 4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])



def transpose(x: np.ndarray) -> np.ndarray:
    def worker(item):
        try:
            transpose_arithmetic(x)
        except:
            print('error with array')


    pool_size = 5

    pool = Pool(pool_size)
     
    array_as_list: np.ndarray = create_list(x)

    for x in enumerate(array_as_list):
        pool.apply_async(worker, (x, ))
    pool.close()
    pool.join()
    return x

def transpose_arithmetic(x: np.ndarray) -> np.ndarray:
    length: int = len(x) 
    if(length == len(x[0])): 
        
        array_as_list: np.ndarray = create_list(x)
        
        newList: np.ndarray = np.arange(length*length)
        k = 0

        for i, val in enumerate(array_as_list):
            if i == (length*length-1): break
            newList[k] = array_as_list[i]
            k = (k + length) % (length*length - 1)

        newList[len(newList)-1] = array_as_list[length*length-1]
        result: np.ndarray = newList.reshape(length, length)
        return result

def add_arrays(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    length_x: int = len(x)
    length_y: int = len(y)

    if(length_x != length_y or len(x) != len(y)):
        return "Warning: You can only add matrices with corresponding dimensions (i.e. 2x2 + 2x2, 3x2 + 3x2)"
    
    newList: np.ndarray = np.arange(length_y*len(y))
    
    array_y_list: np.ndarray = create_list(y)
    array_x_list: np.ndarray = create_list(x)

    
    #TODO: Implement generator that allows me to add each index and abstract for multiplication
    for i, val in enumerate(array_y_list):
        newList[i] = val + array_x_list[i]
        
    result: np.ndarray = newList.reshape(length_y, len(y))
    
    return result



def multiply_matrices(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    lx: int = len(x)
    length_y: int = len(y)-1

    newList: np.ndarray = np.arange(lx*lx)

    array_y: np.ndarray = transpose_arithmetic(y)
    array_x: np.ndarray = x

    j: int = 0    
    
    #TODO: Implement second for loop, which traverses each column using modulus arithmetic and orbit groups

    k: int = 0 
    i: int = 2
    iterator = [(p) % (lx+i) for p in newList]

    print(iterator)
    
'''
    for i in range(length_x-1):
        for p in range(length_x-1):
            while (k+1) != length_x-1:

                newList[j] += array_x[i][k] * array_y[j][k]

                k = k + 1

            k = 0
            j = j + 1
         
    result: np.ndarray = newList.reshape(length_y+2, len(y))

    return result

'''
def create_list(x: np.ndarray) -> list:
    list_of_array = [w for y in x for w in y]
    return list_of_array


print(multiply_matrices(x, y))


#executor = concurrent.futures.ProcessPoolExecutor(10)
#futures = [executor.submit(transpose, x) for x in num]
#concurrent.futures.wait(futures)
