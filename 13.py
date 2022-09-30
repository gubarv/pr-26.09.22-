a17 = ['agbhk', 'fhyfh', 'vnvjv']
a18 = ['fdv', 'ghfuffnd', 'ghgy', 'fhfyf']
a19 = ['jhgdv', 'gfdfffnd', 'jfsy', 'rhryf', 'ggggfd']
print(len(a17)+len(a18)+len(a19), 'общее число студентов!')
if max(a17,a18,a19) == a17:
    print('самая большая группа 17!')
elif max(a17,a18,a19) == a18:
    print('самая большая группа 18!')
elif max(a17,a18,a19) == a19:
    print('самая большая группа 19!')
if min(a17,a18,a19) == a17:
    print('самая маленькая группа 17!')
elif min(a17,a18,a19) == a18:
    print('самая маленькая группа 18!')
elif min(a17,a18,a19) == a19:
    print('самая маленькая группа 19!')
a = a17 + a18 + a19
a.sort()
print(a, 'список студентов в алф порятке!')