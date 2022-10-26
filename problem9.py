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