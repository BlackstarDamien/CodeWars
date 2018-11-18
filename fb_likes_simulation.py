"""
Function, which takes input array which contains names of people, who like an item. Usage example:
likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
"""

def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return '{0} likes this'.format(*names)
    elif len(names) == 3:
        return '{0}, {1} and {2} like this'.format(*names)
    elif len(names) > 3:
        return '{0}, {1}'.format(*names[:2]) + ' and {0} others like this'.format(str(len(names[2:])) if len(names) > 2 else names[2])
    return '{0} and {1} like this'.format(*names)
