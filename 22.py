n = 0
a = [chr(x) for x in range(64, 91)]

with open("22.txt") as f:
    names = sorted(eval(f.read()))
    for name in names:
        n += sum([ord(x)-64 for x in name]) * (names.index(name)+1)

print(n)