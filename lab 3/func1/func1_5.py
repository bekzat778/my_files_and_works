from itertools import permutations
def perm(x):
    permutation = [''.join(p) for p in permutations(x)]
    return permutation

s = "bekzat"

print(perm(s))