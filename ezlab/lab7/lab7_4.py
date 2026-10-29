from lab7 import f4

nums = [int(i) for i in input("Числа через пробел: ").split()]
m = int(input("Порог (неотрицательное целое): "))

print(f"Задание 4 (вариант 10): {f4(nums, m)}")
