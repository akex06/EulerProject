#   UNOPTIMIZED AF
n = 10

while True:
    l = []
    for i in range(1, 21):
        l.append(n % i == 0)

    if all(l):
        print(n)
        break
    print(n)
    n += 1