def isprime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def prime(n):
    n_primes = 0
    prime = 1

    while n_primes < n:
        prime += 1
        if isprime(prime):
            n_primes += 1

    return prime

print(prime(10001))