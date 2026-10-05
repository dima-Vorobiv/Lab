total = int(input("Количество бутылок: "))
capacity = int(input("Бутылок в ящике: "))
print(f"Полных ящиков: {total // capacity}, остаток: {total % capacity}, всего ящиков: {(total + capacity - 1) // capacity}")
