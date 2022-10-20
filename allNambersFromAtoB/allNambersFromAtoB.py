def allNambersFromAtoB(a, b):
    if a < b:
        if a == b:
            print(b)
        else:
            allNambersFromAtoB(a, b-1)
            print(b)
    else:
        if a == b:
            print(b)
        else:
            allNambersFromAtoB(a, b+1)
            print(b)