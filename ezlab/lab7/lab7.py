#Задание 1
def f1(n):
    a = abs(n)
    s = 0
    while a > 0:
        s += a % 10
        a //= 10
    return s

#Задание 2
def f2(n):
    if len(n) == 0:
        return 0
    return sum(n) / len(n)

#Задание 3
def f3(n):
    return " ".join(n.split()).lower()

#Задание 4 (вариант 10)
def f4(n, m):
    return [i for i in n if -m <= i <= 0]
