j = 0
with open("8.txt") as f:
    f = f.read()
    
    for i, c in enumerate(f):
        try:
            l = map(int, list(f[i:i+13]))
            n = 1
            for i in l:
                n *= i

            if n > j:
                j = n

        except:
            pass

print(j)