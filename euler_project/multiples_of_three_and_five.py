def what_are_n():
    storage = []
    container = 0

    while container != -1:
        container = int(input("Enter a number in which you would like to find multiples of: "))

        if container == -1: break
        if type(container) is int and container not in storage:
            storage.append(container)
        elif container in storage:
            print("You have already entered this number, please enter all positive unique integer values")
        else:
            print("You must enter a valid integer that is postive")

    return storage

def __main__():
    #  what_are_n() will return an array of integers
    main_storage = what_are_n()

    #  next we will take a user input for what number they would
    #  like to find the summation of all multiples from storage
    n = int(input("What number would you like to find the multiples of? : "))
    final_arr = []
    

    '''This will loop through n and enter a second for loop that will check
    the mod of each element in final_arr.  We are able to break once finding 
    an element because duplicates would skew the outcome.  Once one number mods
    n, then any other mod that equals 0 is arbitrary to that i'''
    for i in range(0,n): 
        for j, fac in enumerate(main_storage):
            if i % fac == 0:
                final_arr.append(i)
                break

    final = sum(final_arr)        
    print(final)
    

if __name__ == "__main__":
    pass

__main__()