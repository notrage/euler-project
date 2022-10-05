from time import sleep

def problem2():
    """ Return the sum of even-valued fibonacci terms bellow 4000000 """
    somme: int = 2
    current_fibo: int = 0
    fibo_zero: int = 1
    fibo_un: int = 2
    while current_fibo < 4000000:
        current_fibo = fibo_zero + fibo_un
        if current_fibo % 2 ==0: somme += current_fibo
        fibo_zero = fibo_un
        fibo_un = current_fibo
    return somme