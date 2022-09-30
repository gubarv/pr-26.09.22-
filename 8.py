a = [1,1,2,3,3,4,4]
n = 1
for i in range(0, len(a)-1):
    if a[i] != a[i + 1]:
        n += 1
print(n)