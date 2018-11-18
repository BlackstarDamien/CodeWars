"""
Searching max sum inside array of integers
"""

def maxSequence(arr):
    if len(arr) == 0:
        return 0
    total = 0
    for item in arr:
        if item < 0:
            total +=1
    if total == len(arr):
        return 0
    currMaxsum = globalMaxsum = arr[0]
    for x in arr[1:]:
        currMaxsum = max(x, currMaxsum + x)
        globalMaxsum = max(currMaxsum, globalMaxsum)
    return globalMaxsum
