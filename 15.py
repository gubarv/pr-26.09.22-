l = []
n = 10000
while n >= 0:
    if n % 3 == 0 and n % 7 == 0:
        l.append(n)
    elif n % 9 == 0:
        l.append(n)
    n -= 1
print(l)
