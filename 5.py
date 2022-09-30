from random import randrange
k = [randrange(20, 60) for i in range(42)]
с=str(sum(k))
print("Общее число учеников ",с)
if len(с)==4 :
    print(" есть четырехзначное число")
else :
    print(" не является четырехзначным числом")