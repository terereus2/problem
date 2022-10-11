def flip(d, a):
    if d == 'R':
        toRight = sorted(a)
        return toRight
    else:
        toLeft = sorted(a, reverse=True)
        return toLeft