n = int(input())
c = 0
b = -10101001010
summ = 0
for i in range(n):
    a = int(input())
    summ += a
    if a > 0:
        c += 1
    if a > b:
        maxi = a
    b = a
print(summ,c,maxi)
