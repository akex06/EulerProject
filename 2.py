fib = [0, 1]

while fib[-1] <= 4_000_000:
    fib.append(fib[-2]+fib[-1])

print(sum([x for x in fib if x % 2 == 0]))