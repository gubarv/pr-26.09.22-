a = [i for i in range(1, 21)]
for i in range(len(a)):
    if a[i] % 2 == 0:
        a[i] = a[i]**2
    else:
        a[i] = a[i]+2
print(a)