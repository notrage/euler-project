from sympy import isprime
from algorithms import get_divisors
from math import isqrt

def problem_1() -> int:
    """ Return the sum of all the multiples of 3 or 5 bellow 1000 """
    return sum([i for i in range(3,1000) if i%3==0 or i%5==0])

def problem_2() -> int:
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

def problem_3() -> int:
    """ Return the largest prime factor of 600851475143 """
    return max([i for i in [x for x in range(3, int(600851475143**0.5) + 1, 2)] if isprime(i) and 600851475143 % i == 0])

def problem_4() -> int:
    """ Return the largest palindromic product of to numbers of 3 digits each """
    return max(i*j for i in range(1,1000) for j in range(1, 1000) if str(i*j) == str(i*j)[::-1])

def problem_5() -> int:
    """ Return the smallest number divisible by all numbers from 1 to 20 """
    found: bool = False
    i: int = 0
    while not(found):
        i += 20
        if (i%20==0 and i%19==0 and i%18==0 and i%17==0 and i%16==0 and 
            i%15==0 and i%14==0 and i%13==0 and i%12==0 and i%11==0 ): found = True
    return i

def problem_6() -> int:
    """ Return the difference of the sum of 100 first square and the square of the sum of 100 first numbers """
    return sum([i for i in range(1, 101)])**2 - sum([i**2 for i in range(1,101)])

def problem_7() -> int:
    """ Return the 10001th prime number """
    number_prime_found: int = 0
    i: int = 0
    while number_prime_found != 10001:
        if isprime(i):
            number_prime_found += 1
            last_prime = i
        i += 1
    return last_prime

def problem_8() -> int:
    """ Return the thirteen adjacent digits in the 1000-digit number that have the greatest product """
    input: str = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    return max([int(input[i])*int(input[i+1])*int(input[i+2])*int(input[i+3])*int(input[i+4])*int(input[i+5])*
                int(input[i+6])*int(input[i+7])*int(input[i+8])*int(input[i+9])*int(input[i+10])*int(input[i+11])*
                int(input[i+12]) for i in range(0,987)])
    
def problem_9() -> int:
    """ Return a, b and c where a**2 + b**2 = c**2 and where a < b < c """
    return  max([a*b*(a**2+b**2)**0.5 for a in range(1, 998) for b in range(1, 998) if (-a-b+1000) == (a**2+b**2)**0.5])
    """
    Raisonnement mathématique 
    si  a+b+c =1000
        a+b-1000=-c
        c=-a-b+1000
        
    et  a**2+b**2=c**2
        sqrt(a**2+b**2)=c
        c = sqrt(a**2+a**2)

            c               c
    donc -a-b+1000 = sqrt(a**2+b**2)
    """

def problem_10() -> int:
    """ Return the sum of all primes bellow two million """
    return sum([i for i in range(2000000) if isprime(i)])

def problem_11() -> int:
    with open("ressources/problem11.txt", "r") as file: data = [list(map(int, a.split(" "))) for a in file.read().split("\n")]    
    l: list = []
    for i in range(20):
        for j in range(20):
            if i <= 16: l.append(data[i][j]*data[i+1][j]*data[i+2][j]*data[i+3][j])
            if j <= 16: l.append(data[i][j]*data[i][j+1]*data[i][j+2]*data[i][j+3])
            if i <= 16 and j <= 16: l.append(data[i][j]*data[i+1][j+1]*data[i+2][j+2]*data[i+3][j+3])
            if i <= 16 and j >= 3: l.append(data[i][j]*data[i+1][j-1]*data[i+2][j-2]*data[i+3][j-3])
    return max(l)

def problem_12() -> int:
    divisors: list = []
    number: int = 1
    rank: int = 1
    while len(divisors) < 500:
        rank += 1
        number += rank
        divisors = get_divisors(number)
    return number