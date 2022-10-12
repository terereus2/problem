def feastWay1(beast, dish):
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    else:
        return False





def feastWay2(beast, dish):
    if beast[0]+beast[-1] == dish[0]+dish[-1]:
        return True
    else:
        return False
