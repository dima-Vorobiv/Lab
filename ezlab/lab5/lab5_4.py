tex = input("Введите строку: ") # 10 вариант 
countt = 0
words = ""
for i in tex.split():
    clean = i.strip(".,!?;:").lower()
    if len(clean) > 0 and clean[0] == clean[-1]:
        words += clean + " "
        countt += 1
if countt != 0:
    print(f"Слова: {words}")
else:
    print("Нет совпадений")
print(f"Количество: {countt}")
