from sympy import isprime
def problem_10():
    """ Return the sum of all primes bellow two million """
    return sum([i for i in range(2000000) if isprime(i)])