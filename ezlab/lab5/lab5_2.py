tex = input("Введите текст: ")
clean = "".join(tex.split()).lower()
if len(clean) == 0:
    print("Нет текста")
elif clean == clean[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")
