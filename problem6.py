def problem_6():
    """ Return the difference of the sum of 100 first square and the square of the sum of 100 first numbers """
    return sum([i for i in range(1, 101)])**2 - sum([i**2 for i in range(1,101)])