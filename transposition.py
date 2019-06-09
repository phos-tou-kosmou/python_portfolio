#!/bin/python3
import numpy as np
from multiprocessing import Pool

x = np.array([[1, 2, 3, 4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
y = np.array([[1, 2, 3, 4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])



def transpose_multi(x: np.ndarray) -> np.ndarray:
    def worker(item):
        try:
            transpose_arithmetic(x)
        except:
            print('error with array')


    pool_size = 5

    pool = Pool(pool_size)
     
    array_as_list: np.ndarray = create_list(x)

    pool.apply_async(worker, (x, ))
    pool.close()
    pool.join()
    return x

def transpose(x: np.ndarray) -> np.ndarray:
    length: int = len(x) 
    if(length == len(x[0])): 
        
        array_as_list: np.ndarray = create_list(x)
        
        newList: np.ndarray = np.zeros(length*length)
        k = 0

        for i, val in enumerate(array_as_list):
            if i == (length*length-1): break
            newList[k] = array_as_list[i]
            k = (k + length) % (length*length - 1)

        newList[len(newList)-1] = array_as_list[length*length-1]
        result: np.ndarray = newList.reshape(length, length)
        return result

def add_matrices(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    length_x: int = len(x)
    length_y: int = len(y)

    if(length_x != length_y or len(x) != len(y)):
        return "Warning: You can only add matrices with corresponding dimensions (i.e. 2x2 + 2x2, 3x2 + 3x2)"
    
    newList: np.ndarray = np.zeros(length_y*len(y))
    
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

    newList: np.ndarray = np.zeros((lx*lx,), dtype=np.int)

    array_y: np.ndarray = y
    array_x: np.ndarray = x

  #  iterator = [(p) % (lx+i) for p in newList]

  #  print(iterator)

    j: int = 0    
    k: int = 0
    p: int = 0
    
    for i in range(lx):
        for j in range(lx):
            while k < lx:

                newList[p] += array_x[i][k] * array_y[k][j]
                k = k + 1

            k = 0
            p = p + 1
         
    result: np.ndarray = newList.reshape(length_y+1, len(y))

    return result

def determinant(x: np.ndarray) -> np.ndarray:
    '''I have this method here merely to think about
        I believe it would be more beneficial to think about
        QR algorithms, householder matrices, and hessenberg deflations
        mainly becuase determinants are not computed most of the time
        and there are real problems that arise after getting past a
        4x4 matrix'''    


# The return on this method might need to be np.ndarray as well
# hard to tell with duck type 
def create_list(x: np.ndarray) -> list:
    list_of_array: np.ndarray = [w for y in x for w in y]
    return list_of_array

print(transpose(x))

#print(multiply_matrices(transpose_arithmetic(x), y))


#executor = concurrent.futures.ProcessPoolExecutor(10)
#futures = [executor.submit(transpose, x) for x in num]
#concurrent.futures.wait(futures)
