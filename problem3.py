from sympy import isprime
def problem_3() -> int:
    """ Return the largest prime factor of 600851475143 """
    return max([i for i in [x for x in range(3, int(600851475143**0.5) + 1, 2)] if isprime(i) and 600851475143 % i == 0])