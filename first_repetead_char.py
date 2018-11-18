"""
Function, that returns the first character that repeats in a String.
"""

def first_dup(s):
    for item in range(0, len(s)-1):
        if s[item] in s[item+1:] and isinstance(s[item], str):
            return s[item]
    return None
