a = list(range(1, 101))
i = 0
l = []

while i < len(a):
    if a[i] % 7 == 0 and a[i] % 5 != 0:
        l.append(a[i])
    i += 1

print(l)
