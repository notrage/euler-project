def problem4():
    """ Return the largest palindromic product of to numbers of 3 digits each """
    return max(i*j for i in range(1,1000) for j in range(1, 1000) if str(i*j) == str(i*j)[::-1])