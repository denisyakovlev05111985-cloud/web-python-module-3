def print_grades(grades):
    """Вывод оценок (содержимого списка)"""
    print("\nОценки студента:")
    for i, grade in enumerate(grades, 1):
        print(f"{i}. {grade}")

def retake_exam(grades):
    """Пересдача экзамена — изменение оценки по номеру"""
    try:
        index = int(input("Введите номер оценки для пересдачи (1-10): ")) - 1
        if 0 <= index < len(grades):
            new_grade = int(input("Введите новую оценку (1-12): "))
            if 1 <= new_grade <= 12:
                grades[index] = new_grade
                print(f"Оценка №{index + 1} успешно изменена на {new_grade}.")
            else:
                print("Ошибка: оценка должна быть от 1 до 12.")
        else:
            print("Ошибка: неверный номер оценки.")
    except ValueError:
        print("Ошибка: введите целое число.")

def check_scholarship(grades):
    """Проверка, выходит ли стипендия (средний балл >= 10.7)"""
    average = sum(grades) / len(grades)
    print(f"\nСредний балл: {average:.2f}")
    if average >= 10.7:
        print("Стипендия ВЫХОДИТ!")
    else:
        print("Стипендия НЕ выходит.")

def sort_grades(grades):
    """Сортировка списка оценок по возрастанию или убыванию"""
    choice = input("Сортировать по возрастанию (в) или убыванию (у)? (в/у): ").strip().lower()
    sorted_grades = sorted(grades, reverse=(choice == 'у'))
    order_name = "убыванию" if choice == 'у' else "возрастанию"
    print(f"\nОценки, отсортированные по {order_name}:")
    print(", ".join(map(str, sorted_grades)))

def main():
    # Ввод 10 оценок от пользователя
    print("Введите 10 оценок студента (от 1 до 12):")
    grades = []
    for i in range(10):
        while True:
            try:
                grade = int(input(f"Оценка {i + 1}: "))
                if 1 <= grade <= 12:
                    grades.append(grade)
                    break
                else:
                    print("Оценка должна быть от 1 до 12. Попробуйте снова.")
            except ValueError:
                print("Пожалуйста, введите целое число.")

    # Главное меню
    while True:
        print("\n" + "="*40)
        print("МЕНЮ УСПЕВАЕМОСТИ")
        print("="*40)
        print("1. Вывод оценок")
        print("2. Пересдача экзамена")
        print("3. Проверка стипендии")
        print("4. Сортировка оценок")
        print("5. Выход")
        print("-"*40)

        choice = input("Выберите пункт меню (1-5): ").strip()

        if choice == '1':
            print_grades(grades)
        elif choice == '2':
            retake_exam(grades)
        elif choice == '3':
            check_scholarship(grades)
        elif choice == '4':
            sort_grades(grades)
        elif choice == '5':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите число от 1 до 5.")

if __name__ == "__main__":
    main()
