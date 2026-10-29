nums = [int(i) for i in input("Целые числа через пробел: ").split()]
if len(nums) == 0:
    print("Нет данных")
else:
    maxx = max(nums)
    res = [i for i in range(len(nums)) if nums[i] == maxx]
    print(f"Индексы максимума: {res}")
