"""def get_divisors(n):
    D = []
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            D.append(i)
            D.append(n//i)
    return sorted(set(D))"""
    
def get_divisors(n): return sorted(set([i[j] for i in [[i, n//i] for i in range(1, int(n**0.5) + 1) if n%i == 0] for j in range(2)]))

