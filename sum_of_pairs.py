"""
Function, which return the first two values (parsed from the left) in order of appearance that add up to form the sum.
"""

def sum_pairs(ints, s):
    memo = {}
    results = []
    for i in range(0,len(ints)):
        sum = s - ints[i]
        if sum in memo:
            results.append([sum, ints[i]])
        memo[ints[i]] = ints[i]
    if len(results) == 0:
        return None
    return min(results)
