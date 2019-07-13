def sum_of_squares(n):
    return (n*(n+1)*(2*n+1)) / 6

def square_of_sum(n):
    container = 0
    for i in range(1, n):
        container += i
    return container*container

def __main__():

    num = int(input("Enter a positive integer: "))
    final = 0
    
    ss = sum_of_squares(num)
    sq = square_of_sum(num)
    final = sq - ss

    print(final)

if __name__ == "__main__":
    pass

__main__()