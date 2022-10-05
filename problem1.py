def problem1():
    """ Return the sum of all the multiples of 3 or 5 bellow 1000 """
    #sum = 0
    #for i in range(1, 1000):
    #    if i % 3 == 0 or i % 5 == 0: sum += i
    #return sum
    return sum([i for i in range(3,1000) if i%3==0 or i%5==0])