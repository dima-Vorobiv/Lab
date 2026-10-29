from lab7 import f2

nums = [int(i) for i in input("Числа через пробел: ").split()]

if len(nums) == 0:
    print("Нет данных")
else:
    print(f"Среднее: {f2(nums)}")
