from sympy import FourierTransform


def problem5():
    """ Return the smallest number divisible by all numbers from 1 to 20 """
    found: bool = False
    i: int = 0
    while not(found):
        i += 20
        if (i%20==0 and i%19==0 and i%18==0 and i%17==0 and i%16==0 and 
            i%15==0 and i%14==0 and i%13==0 and i%12==0 and i%11==0 ): found = True
    return i