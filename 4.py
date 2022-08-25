
l = [0, 0]

for i in range(1, 1000):
    for j in range(1, 1000):
        a = str(i * j)

        if a == a[::-1]:
            if int(a) > l[0] * l[1]:
                l = [i, j]

print(l[0] * l[1])