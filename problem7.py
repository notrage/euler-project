from sympy import isprime
def problem_7():
    """ Return the 10001th prime number """
    number_prime_found: int = 0
    i: int = 0
    while number_prime_found != 10001:
        if isprime(i):
            number_prime_found += 1
            last_prime = i
        i += 1
    return last_prime