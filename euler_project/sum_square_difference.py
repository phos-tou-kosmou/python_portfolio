def sum_of_squares(n):
    return (n*(n+1)*(2*n+1)) / 6

def square_of_sum(n):
    container = 0
    for i in range(1, n):
        container += i
    container = container + n
    return container*container

def validate_input(n):
    if type(n) is int:
        if n > 0:
            return True
    return False

def __main__():
    j = None
    while j != 1:
        num = int(input("Enter a positive integer: "))
    
        if validate_input(num):
            break
        else:
            print("input is not valid")

    
    final = 0
    
    ss = sum_of_squares(num)
    sq = square_of_sum(num)
    final = sq - ss

    print(final)

if __name__ == "__main__":
    pass

__main__()