# Написатьпрограмму«справочник».Создатьдвасписка 
# целых. Один список хранит идентификационные коды, 
# второй — телефонные номера. Реализовать меню для 
# пользователя:

# ■ Отсортировать по идентификационным кодам;

# ■ Отсортировать по номерам телефона;

# ■ Вывестисписокпользователейскодамиителефонами;

# ■ Выход


# Создаем два списка для хранения данных

ids = []
phones = []

def add_user():
    """Добавление нового пользователя"""
    try:
        id = int(input("Введите идентификационный код: "))
        phone = input("Введите номер телефона: ")
        
        # Проверяем уникальность идентификатора
        if id in ids:
            print("Такой идентификатор уже существует!")
            return
            
        ids.append(id)
        phones.append(phone)
        print("Пользователь добавлен!")
    except ValueError:
        print("Ошибка: введите целое число для идентификатора!")

def sort_by_id():
    """Сортировка по идентификаторам"""
    ids.sort()
    print("\nСписок отсортирован по ID:")
    for i in range(len(ids)):
        print(f"{ids[i]} - {phones[i]}")

def sort_by_phone():
    """Сортировка по номерам телефонов"""
    # Сортируем по номерам, сохраняя соответствие ID и телефона
    sorted_list = sorted(zip(ids, phones), key=lambda x: x[1])
    print("\nСписок отсортирован по номерам:")
    for id, phone in sorted_list:
        print(f"{id} - {phone}")

def show_all():
    """Вывод всех пользователей"""
    if not ids:
        print("Список пуст!")
        return
    print("\nСписок пользователей:")
    for i in range(len(ids)):
        print(f"{ids[i]} - {phones[i]}")

def main_menu():
    while True:
        print("\nСправочник пользователей")
        print("1. Добавить пользователя")
        print("2. Отсортировать по ID")
        print("3. Отсортировать по номеру")
        print("4. Показать всех")
        print("5. Выход")
        choice = input("Выберите действие: ")
        
        if choice == '1':
            add_user()
        elif choice == '2':
            sort_by_id()
        elif choice == '3':
            sort_by_phone()
        elif choice == '4':
            show_all()
        elif choice == '5':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()
