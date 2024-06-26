def is_prime(n):
    prime = True
    for j in range(2,int(n**0.5)+1):
        if n % j == 0:
            prime = False
            break
    return prime


def factor(n):
    if not isinstance(n, int):
        raise TypeError()
    if n <= 1:
        raise Exception()
    d = {}
    m = int(n**0.5)
    i = 2
    while i <= m+1:        
        if n % i == 0 and is_prime(i):
            d[i] = 0
            while n % i == 0:
                d[i] += 1
                n = n // i
        i += 1
    return d

