# Создаем два списка для хранения книг
books = [
    {"title": "Война и мир", "year": 1869},
    {"title": "Преступление и наказание", "year": 1866},
    {"title": "Мастер и Маргарита", "year": 1966},
    {"title": "1984", "year": 1949},
    {"title": "Унесенные ветром", "year": 1936}
]

# Функция для сортировки книг по названию
def sort_by_title(books):
    return sorted(books, key=lambda x: x["title"])

# Функция для сортировки по году выпуска
def sort_by_year(books):
    return sorted(books, key=lambda x: x["year"])

def main_menu():
    while True:
        print("\nМеню:")
        print("1. Отсортировать по названию книг")
        print("2. Отсортировать по годам выпуска")
        print("3. Вывести список книг с названиями и годами")
        print("4. Выход")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == '1':
            sorted_books = sort_by_title(books)
            print("\nКниги, отсортированные по названию:")
            for book in sorted_books:
                print(f"{book['title']} ({book['year']})")
                
        elif choice == '2':
            sorted_books = sort_by_year(books)
            print("\nКниги, отсортированные по году:")
            for book in sorted_books:
                print(f"{book['title']} ({book['year']})")
                
        elif choice == '3':
            print("\nСписок книг:")
            for book in books:
                print(f"{book['title']} ({book['year']})")
                
        elif choice == '4':
            print("До свидания!")
            break
            
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main_menu()
