"""
Converts string to camel case
"""

import re
def to_camel_case(text):
    return re.sub('(?:_|-)[?:a-z|A-Z]', lambda x: x.group()[1].upper(), text)
