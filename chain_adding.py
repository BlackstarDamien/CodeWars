"""
Example function, which shows currying in Python
"""

def add(x):
    class CustomInt(int):
        def __call__(self, v):
            return CustomInt(self + v)
    return CustomInt(x)
