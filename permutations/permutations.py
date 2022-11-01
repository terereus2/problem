import itertools


def permutations(s):
    all_permutations = itertools.permutations(s, len(s))
    set_of_permutations = set([''.join(elem) for elem in all_permutations])
    return list(set_of_permutations)
