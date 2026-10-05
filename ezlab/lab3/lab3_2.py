a = int(input())
b = int(input())
znak = input()
if znak == '+':
    print(a+b)
if znak == '-':
    print(a-b)
if znak == '*':
    print(a*b)
if znak == '/' and b != 0:
    print(f'{a/b:.2f}')
else: print('ошибка в переменных')
