x = int(input())
y = int(input())
if 0 <= x <= 5 and 0 <= y <= 3:
    if (x == 5 or x == 0) and (y == 0 or y == 3):
        print('На границе')
    else: print('Внутри')
else:print('Снаружи')
        
