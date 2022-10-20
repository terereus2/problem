def allNambers(x):
    if x == 1:
       print(x)
    else:
        allNambers(x-1)
        print(x)
        