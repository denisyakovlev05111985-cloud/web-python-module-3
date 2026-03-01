import os
import json

class Employee:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.surname} {self.name}, {self.age} лет"

    def to_dict(self):
        return {
            'surname': self.surname,
            'name': self.name,
            'age': self.age
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['surname'], data['name'], data['age'])


class EmployeeSystem:
    def __init__(self, file_name):
        self.file_name = file_name
        self.employees = self.load_employees_from_file()

    def load_employees_from_file(self):
        """Загрузка сотрудников из файла при старте программы"""
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    return [Employee.from_dict(emp) for emp in data]
            except (json.JSONDecodeError, IOError):
                print("Ошибка при чтении файла. Создан пустой список сотрудников.")
                return []
        else:
            print("Файл не найден. Создан пустой список сотрудников.")
            return []

    def save_employees_to_file(self, filename=None):
        """Сохранение всех сотрудников в файл"""
        save_file = filename or self.file_name
        try:
            with open(save_file, 'w', encoding='utf-8') as file:
                data = [emp.to_dict() for emp in self.employees]
                json.dump(data, file, ensure_ascii=False, indent=2)
            print(f"Список сотрудников сохранён в файл: {save_file}")
        except IOError as e:
            print(f"Ошибка при сохранении файла: {e}")

    def add_employee(self, surname, name, age):
        """Добавление нового сотрудника"""
        new_employee = Employee(surname, name, age)
        self.employees.append(new_employee)
        print(f"Сотрудник {surname} {name} добавлен.")

    def edit_employee(self, surname, new_name=None, new_age=None):
        """Редактирование данных сотрудника"""
        for employee in self.employees:
            if employee.surname == surname:
                if new_name:
                    employee.name = new_name
                if new_age:
                    employee.age = new_age
                print(f"Данные сотрудника {surname} обновлены.")
                return
        print("Сотрудник не найден.")

    def delete_employee(self, surname):
        """Удаление сотрудника по фамилии"""
        for i, employee in enumerate(self.employees):
            if employee.surname == surname:
                del self.employees[i]
                print(f"Сотрудник {surname} удалён.")
                return
        print("Сотрудник не найден.")

    def find_by_surname(self, surname_part):
        """Поиск сотрудников по части фамилии"""
        results = [emp for emp in self.employees if emp.surname.lower().startswith(surname_part.lower())]
        return results

    def find_by_age(self, age):
        """Поиск сотрудников определённого возраста"""
        results = [emp for emp in self.employees if emp.age == age]
        return results

    def print_employees(self, employees):
        """Вывод списка сотрудников"""
        if not employees:
            print("Сотрудники не найдены.")
            return

        print(f"\nНайдено сотрудников: {len(employees)}")
        print("-" * 30)
        for emp in employees:
            print(emp)
        print()

    def save_search_results(self, employees, filename):
        """Сохранение результатов поиска в файл"""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                for emp in employees:
                    file.write(f"{emp}\n")
            print(f"Результаты поиска сохранены в файл: {filename}")
        except IOError as e:
            print(f"Ошибка при сохранении результатов: {e}")

def main():
    file_name = input("Введите имя файла для загрузки списка сотрудников: ")
    system = EmployeeSystem(file_name)

    while True:
        print("\n" + "="*40)
        print("ИНФОРМАЦИОННАЯ СИСТЕМА «СОТРУДНИКИ»")
        print("="*40)
        print("1. Добавить сотрудника")
        print("2. Редактировать сотрудника")
        print("3. Удалить сотрудника")
        print("4. Найти сотрудника по фамилии")
        print("5. Найти сотрудников по возрасту")
        print("6. Вывести информацию обо всех сотрудниках")
        print("7. Сохранить список сотрудников в файл")
        print("8. Сохранить результаты поиска в файл")
        print("9. Выход")

        choice = input("\nВведите номер пункта меню: ").strip()

        if choice == "1":
            surname = input("Введите фамилию: ").strip()
            name = input("Введите имя: ").strip()
            try:
                age = int(input("Введите возраст: ").strip())
                system.add_employee(surname, name, age)
            except ValueError:
                print("Возраст должен быть числом!")

        elif choice == "2":
            surname = input("Введите фамилию сотрудника для редактирования: ").strip()
            new_name = input("Введите новое имя (оставить пустым, если не менять): ").strip() or None
            new_age_input = input("Введите новый возраст (оставить пустым, если не менять): ").strip()
            new_age = int(new_age_input) if new_age_input else None
            system.edit_employee(surname, new_name, new_age)

        elif choice == "3":
            surname = input("Введите фамилию сотрудника для удаления: ").strip()
            system.delete_employee(surname)

        elif choice == "4":
            surname_part = input("Введите начало фамилии для поиска: ").strip()
            results = system.find_by_surname(surname_part)
            system.print_employees(results)
            if results and input("Сохранить результаты поиска в файл? (д/н): ").lower() == 'д':
                filename = input("Введите имя файла для сохранения: ").strip()
                system.save_search_results(results, filename)

        elif choice == "5":
            try:
                age = int(input("Введите возраст для поиска: ").strip())
                results = system.find_by_age(age)
                system.print_employees(results)
                if results and input("Сохранить результаты поиска в файл? (д/н): ").lower() == 'д':
                    filename = input("Введите имя файла для сохранения: ").strip()
                    system.save_search_results(results, filename)
            except ValueError:
                print("Возраст должен быть числом!")

        elif choice == "6":
            system.print_employees(system.employees)

        elif choice == "7":
            filename = input("Введите имя файла для сохранения списка сотрудников: ").strip()
            system.save_employees_to_file(filename)

        elif choice == "8":
            if not system.employees:
                print("Список сотрудников пуст!")
                continue
            filename = input("Введите имя файла для сохранения всех сотрудников: ").strip()
            system.save_employees_to_file(filename)

        elif choice == "9":
            system.save_employees_to_file()
            print("Данные сохранены. Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
