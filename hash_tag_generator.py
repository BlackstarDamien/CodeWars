"""
Script that generating hashtags. This is solution for kata The Hastag Generator
from CodeWars.com
"""

def generate_hashtag(s):
    if len(s) == 0 or len(s) > 140:
        return False
    return '#' + ''.join(map(lambda x: str.capitalize(x),[i for i in s.split()]))
