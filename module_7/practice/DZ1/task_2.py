# Создаем пустой словарь для хранения пар слов
dictionary = {}

def add_word():
    """Добавление слова в словарь"""
    english = input("Введите английское слово: ")
    french = input("Введите французский перевод: ")
    dictionary[english] = french
    print("Слово успешно добавлено!")

def remove_word():
    """Удаление слова из словаря"""
    word = input("Введите слово для удаления: ")
    if word in dictionary:
        del dictionary[word]
        print("Слово удалено!")
    else:
        print("Такого слова нет в словаре!")

def search_word():
    """Поиск слова в словаре"""
    search_word = input("Введите слово для поиска: ")
    if search_word in dictionary:
        print(f"Перевод: {dictionary[search_word]}")
    else:
        print("Слово не найдено!")

def replace_word():
    """Замена существующего перевода"""
    old_word = input("Старое слово: ")
    new_word = input("Новый перевод: ")
    if old_word in dictionary:
        dictionary[old_word] = new_word
        print("Перевод успешно заменен!")
    else:
        print("Такого слова нет в словаре!")

# Главное меню программы
while True:
    print("\nАнгло-французский словарь")
    print("1. Добавить слово")
    print("2. Удалить слово")
    print("3. Найти слово")
    print("4. Заменить перевод")
    print("5. Выход")
    
    choice = input("Выберите действие: ")
    
    if choice == '1':
        add_word()
    elif choice == '2':
        remove_word()
    elif choice == '3':
        search_word()
    elif choice == '4':
        replace_word()
    elif choice == '5':
        print("До свидания!")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
