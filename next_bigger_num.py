"""
function that takes a positive integer number and returns the next bigger number formed by the same digits
"""

def next_bigger(n):
    s = list(str(n))
    for i in reversed(range(1, len(s))):
        if s[i] > s[i - 1]:
            pos = i - 1
            for j in reversed(range(pos + 1, len(s))):
                if s[j] > s[pos]:
                    s[pos], s[j] = s[j], s[pos]
                    s[pos + 1:] = s[pos + 1:][::-1]
                    break
            return int(''.join(s))
    return -1
