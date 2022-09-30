a = [1,2,3,4]
for i in range(len(a)):
    if a[i] % 2 == 0:
        a[i] = a[i]*-1
s = 0
for i in range(len(a)):
    s += a[i]
print(s)


