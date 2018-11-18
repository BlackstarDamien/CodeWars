"""
function, which strip comments and whitespaces from the end of string
"""

def strip_comments(string, markers):
    res = string.split('\n')
    for i, item in enumerate(res):
        for m in markers:
            idx = item.find(m)
            if idx != -1:
                item = item[:idx]
        res[i] = item.rstrip(" ")
    return "\n".join(res)
