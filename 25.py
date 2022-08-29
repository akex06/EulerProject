n = 1
fibo = [1, 1]

while True:
    if len(str(fibo[-1])) >= 1000:
        print(n+1)
        break

    fibo.append(sum(fibo[-2:]))
    n += 1