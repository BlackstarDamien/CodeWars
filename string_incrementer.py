"""
 Function which increments a string, to create a new string. If the string already ends with a number, the number is incremented by 1.
 If the string does not end with a number the number 1 is appended to the new string.
"""
import re
def increment_string(strng):
    if len(re.findall('\d+$', strng)) == 0:
        return strng + '1'
    else:
        a = len(str(re.findall('\d+$', strng)[0]))
        return ''.join([i for i in strng.replace(re.findall('\d+$', strng)[0], '')]) + str(int(str(re.findall('\d+$', strng)[0]))+1).zfill(a)
