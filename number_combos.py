"""
 Function,that accepts a single positive integer n (30 > n > 0)
 and returns an array of arrays of positive integers that sum to n.
"""

def combos(n):
    def c(n):
        if n == 0:
            yield []
            return

        for p in c(n - 1):
            yield [1] + p
            if p and (len(p) < 2 or p[1] > p[0]):
                yield [p[0] + 1] + p[1:]
    return list(c(n))
