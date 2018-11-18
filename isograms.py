"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive.
"""

def is_isogram(string):
    string = string.lower()
    for item in string:
        c = string.count(item)
        if c > 1:
            return False
            break
    return True
