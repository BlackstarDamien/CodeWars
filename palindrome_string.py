"""
function, which generate palindrome string
"""

palindrome=lambda n,s:(s*n)[:n//2]+(s*n)[~-n//2::-1]
