l = []
for i in range(2, 2000001):
    print(i)
    t = []
    for j in range(2, i):
        t.append(i % j != 0)

    if all(t):
        l.append(i)

print(sum(l))