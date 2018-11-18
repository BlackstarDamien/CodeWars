"""
Method that takes an array of consecutive (increasing) letters as input
and that returns the missing letter in the array.
"""

import string

def find_missing_letter(chars):
    charset = string.ascii_lowercase if chars[0] >= 'a' else string.ascii_uppercase
    for letter in charset[charset.index(chars[0]):]:
        if letter not in chars:
            return letter[0]
