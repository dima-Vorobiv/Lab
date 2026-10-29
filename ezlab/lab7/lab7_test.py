from lab7 import f1, f2, f3, f4

#Задание 1
assert f1(0) == 0
assert f1(507) == 12
assert f1(-507) == 12

#Задание 2
assert f2([]) == 0
assert f2([2, 4, 6]) == 4

#Задание 3
assert f3(" HELLO World ") == "hello world"
assert f3("   ") == ""

#Задание 4 (вариант 10)
assert f4([-5, 0, 2, 5], 2) == [0]
assert f4([], 2) == []
assert f4([0, 0, -2], 2) == [0, 0, -2]
assert f4([-3, 1], 2) == []

print("Все проверки пройдены")
