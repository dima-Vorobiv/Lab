predmet1 = input("Первый предмет: ")
zanyatiy1 = int(input("Количество занятий по первому предмету за неделю: "))
time1 = int(input("Продолжительность одного занятия первого предмета (мин): "))
predmet2 = input("Второй предмет: ")
zanyatiy2 = int(input("Количество занятий по второму предмету за неделю: "))
time2 = int(input("Продолжительность одного занятия второго предмета (мин): "))
free_time = float(input("Доступное время на неделю (часы): "))
vsego_min1 = zanyatiy1 * time1
vsego_min2 = zanyatiy2 * time2
vsego_min = vsego_min1 + vsego_min2
vsego_chasov = vsego_min / 60
ostatok_svobodnogo = free_time - vsego_chasov
za4 = vsego_min * 4
print(f"{predmet1}: {vsego_min1} мин")
print(f"{predmet2}: {vsego_min2} мин")
print(f"Общая нагрузка: {vsego_min} мин = {vsego_chasov:.2f} ч")
print(f"Остаток свободного времени: {ostatok_svobodnogo:.2f} ч")
print(f"Нагрузка за 4 недели: {za4} мин = {za4 / 60:.2f} ч")
