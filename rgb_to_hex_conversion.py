def rgb(r, g, b):
    a = [r,g,b]
    i = 0
    for item in a:
        if item < 0:
            a[i] = 0
        elif item > 255:
            a[i] = 255
        i += 1
    args = [hex(i).split('x')[-1].upper() for i in a]
    b = 0
    for item in args:
        if len(item) == 1:
            args[b] = '0' + str(item)
        b += 1
    return '{}{}{}'.format(*args)
