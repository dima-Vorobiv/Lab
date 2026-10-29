nums = [int(i) for i in input("Целые числа через пробел: ").split()]
res = [abs(i) for i in nums]
print(f"Исходный список: {nums}")
print(f"Новый список: {res}")
