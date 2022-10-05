from time import sleep

def problem2():
    """ Return the sum of fibonacci terms bellow 4000000 """
    s: int = 0
    i: int = 0
    a: int = 1
    b: int = 2
    while i < 4000000:
        s += i
        a = b + i
        b = a + i
        i = a + b
    return s