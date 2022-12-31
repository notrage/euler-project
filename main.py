from time import time
from problems import *
from algorithms import get_divisors

if __name__ == "__main__":
    t = time()
    print(problem_12())
    print("temps d'exécution:", time()-t,"secondes.")