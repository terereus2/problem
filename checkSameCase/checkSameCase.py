import string


def same_case(a, b):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    if ((a in upper) and (b in upper)) or ((a in lower) and (b in lower)):
        return 1
    elif ((a in upper) and (b in lower)) or ((a in lower) and (b in upper)):
        return 0
    else:
        return -1
