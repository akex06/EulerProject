f = 600851475143
primes = []
n = 2
while True:
    prime = all([n % x != 0 for x in range(2, n)])
    if prime:
        primes.append(n)
    
        for i in primes[::-1]:
            if f % i == 0:
                f //= i

            if f == 1:
                print(n)
                exit()

    n += 1