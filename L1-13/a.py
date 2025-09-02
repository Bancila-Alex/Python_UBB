#a. Determine the first (and only) 8 natural numbers (x1, x2,  …,  x8) greater than 2
# with the following property: all the natural numbers smaller than xi and that are relatively prime with xi
# (except for the number 1) are prime, i =1,2, …, n.

def relatively_prime(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a == 1

def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def solution():
    solutions = 0
    value = 3
    while solutions < 8:
        is_solution = True
        for number in range(2, value):
            if relatively_prime(number,value):
                if not prime(number):
                    is_solution = False
        if is_solution:
            print(value, end=" ")
            solutions += 1
        value += 1

if __name__ == "__main__":
    solution()