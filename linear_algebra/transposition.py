#!/bin/python3
import numpy as np
from multiprocessing import Pool
import threading

x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
y = np.array([[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]])


def transpose_multi(arr: np.ndarray) -> np.ndarray:
    def worker(item):
        try:
            transpose(arr)
        except:
            print('error with array')

    pool_size = 5

    pool = Pool(pool_size)

    # array_as_list: np.ndarray = create_list(x)

    pool.apply_async(worker, (x,))
    pool.close()
    pool.join()
    return x


def transpose(tx: np.ndarray) -> np.ndarray:
    length: int = len(tx)
    if length == len(tx[0]):

        array_as_list: list = create_list(tx)

        newList: np.ndarray = np.zeros(length * length)
        k = 0

        for i, val in enumerate(array_as_list):
            if i == (length * length - 1): break
            newList[k] = array_as_list[i]
            k = (k + length) % (length * length - 1)

        newList[len(newList) - 1] = array_as_list[length * length - 1]
        result: np.ndarray = newList.reshape(length, length)
        print(result)


def add_matrices(amx: np.ndarray, amy: np.ndarray) -> np.ndarray:
    length_x: int = len(amx)
    length_y: int = len(amy)

    if length_x != length_y or len(amx) != len(amy):
        return "Warning: You can only add matrices with corresponding dimensions (i.e. 2x2 + 2x2, 3x2 + 3x2)"

    newList: np.ndarray = np.zeros(length_y * len(y))

    array_y_list: list = create_list(y)
    array_x_list: list = create_list(x)

    # TODO: Implement generator that allows me to add each index and abstract for multiplication
    for i, val in enumerate(array_y_list):
        newList[i] = val + array_x_list[i]

    result: np.ndarray = newList.reshape(length_y, len(y))

    return result


def multiply_matrices(mmx: np.ndarray, mmy: np.ndarray) -> np.ndarray:
    lx: int = len(mmx)
    length_y: int = len(mmy) - 1

    newList: np.ndarray = np.zeros((lx * lx,), dtype=np.int)

    array_y: np.ndarray = mmy
    array_x: np.ndarray = mmx

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

    result: np.ndarray = newList.reshape(length_y + 1, len(y))

    return result


def create_list(oldarr: np.ndarray) -> list:
    list_of_array: list = [w for p in oldarr for w in p]
    return list_of_array


if __name__ == '__main__':
    thread1 = threading.Thread(target=transpose(x), args=(10,))
    thread2 = threading.Thread(target=transpose(y), args=(10,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


# print(multiply_matrices(transpose_arithmetic(x), y))


# executor = concurrent.futures.ProcessPoolExecutor(10)
# futures = [executor.submit(transpose, x) for x in num]
# concurrent.futures.wait(futures)
