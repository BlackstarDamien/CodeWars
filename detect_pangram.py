"""
Function, which detecting pangrams
"""

import string

def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return not (set(alphabet) - set(''.join(s.translate(str.maketrans("!?,.:", 5*' ')).split()).lower()))
