n = int(input())
c = 0
summ = 0
for i in range(n):
    a = int(input())
    if a >= 10:
        c +=1
        summ = summ + a
print(c,summ)
