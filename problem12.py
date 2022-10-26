def problem_12() -> int:
    divisors: list = []
    number: int = 1
    rank: int = 1
    while len(set(divisors)) < 500:
        rank += 1
        divisors = []
        for i in range(1, int(number**0.5)+1):
            if number%i == 0: 
                divisors.append(i)
                divisors.append(number//i)
        number += rank
    return number