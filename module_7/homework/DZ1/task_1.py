# Создаем пустой словарь для хранения данных
basketball_players = {}

def add_player():
    """Добавление нового игрока"""
    name = input("Введите ФИО игрока: ")
    height = float(input("Введите рост игрока (в см): "))
    basketball_players[name] = height
    print(f"Игрок {name} добавлен!")

def delete_player():
    """Удаление игрока по ФИО"""
    name = input("Введите ФИО игрока для удаления: ")
    if name in basketball_players:
        del basketball_players[name]
        print(f"Игрок {name} удален!")
    else:
        print("Игрок не найден!")

def find_player():
    """Поиск игрока по ФИО"""
    name = input("Введите ФИО игрока для поиска: ")
    if name in basketball_players:
        print(f"Найден игрок: {name}, рост: {basketball_players[name]} см")
    else:
        print("Игрок не найден!")

def replace_player():
    """Замена данных игрока"""
    old_name = input("Введите старое ФИО игрока: ")
    new_name = input("Введите новое ФИО игрока: ")
    
    if old_name in basketball_players:
        basketball_players[new_name] = basketball_players.pop(old_name)
        print(f"Данные игрока {old_name} заменены на {new_name}")
    else:
        print("Игрок не найден!")

# Главное меню программы
while True:
    print("\nМеню:")
    print("1. Добавить игрока")
    print("2. Удалить игрока")
    print("3. Найти игрока")
    print("4. Заменить данные игрока")
    print("5. Выход")
    
    choice = input("Выберите действие: ")
    
    if choice == '1':
        add_player()
    elif choice == '2':
        delete_player()
    elif choice == '3':
        find_player()
    elif choice == '4':
        replace_player()
    elif choice == '5':
        print("До свидания!")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
