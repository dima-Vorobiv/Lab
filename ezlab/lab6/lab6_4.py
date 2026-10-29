nums = [int(i) for i in input("Целые числа через пробел: ").split()]
res = [i for i in nums if i >= 10]
print(f"Исходный список: {nums}")
print(f"Выборка (в исходном порядке): {res}")
print(f"Количество: {len(res)}")
print(f"Сумма: {sum(res)}")
print(f"Сортированная копия: {sorted(res)}")
