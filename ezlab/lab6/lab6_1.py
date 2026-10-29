nums = [int(i) for i in input("Целые числа через пробел: ").split()]
if len(nums) == 0:
    print("Нет данных")
else:
    print(f"Количество: {len(nums)}")
    print(f"Сумма: {sum(nums)}")
    print(f"Минимум: {min(nums)}")
    print(f"Максимум: {max(nums)}")
    print(f"Среднее: {sum(nums) / len(nums):.2f}")
