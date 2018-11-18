"""
Function which creates all permutations of input without duplicates
"""

def permutations(string):
    res = [string]
    for i, c in enumerate(string):
        for s in permutations(string[:i] + string[i + 1:]):
            res.append(c + s)
    return set(res)
