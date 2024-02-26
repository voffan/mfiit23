def factor(n):
    if not isinstance(n, int):
        raise TypeError()
    d = {}
    m = int(n**0.5)
    for i in range(2,m+1):
        prime = True
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                prime = False
                break
        if n % i == 0 and prime:
            d[i] = 0
            while n % i == 0:
                d[i] += 1
                n = n // i
    return d
