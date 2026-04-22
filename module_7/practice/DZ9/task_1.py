# Напишитеинформационнуюсистему«Сотрудники». 
# Программадолжнаобеспечиватьвводданных,редакти
# рованиеданныхсотрудника,удалениесотрудника,поиск 
# сотрудника по фамилии, вывод информации обо всех 
# сотрудниках, указанноговозраста, или фамилиякоторых 
# начинаетсянауказаннуюбукву.Организуйтевозможность 
# сохранения найденной информации в файл. Также весь 
# список сотрудников сохраняется в файл (при выходе из 
# программы — автоматически, в процессе исполнения 
# программы — по команде пользователя). При старте 
# программыпроисходит загрузка списка сотрудников из 
# указанного пользователем файла


import json
import os
from datetime import datetime

class Employee:
    def __init__(self, id, last_name, first_name, middle_name, birth_year, position, salary):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.birth_year = birth_year
        self.position = position
        self.salary = salary

    def to_dict(self):
        return {
            'id': self.id,
            'last_name': self.last_name,
            'first_name': self.first_name,
            'middle_name': self.middle_name,
            'birth_year': self.birth_year,
            'position': self.position,
            'salary': self.salary
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['id'],
            data['last_name'],
            data['first_name'],
            data['middle_name'],
            data['birth_year'],
            data['position'],
            data['salary']
        )

    def get_age(self, current_year=None):
        if current_year is None:
            current_year = datetime.now().year
        return current_year - self.birth_year

    def __str__(self):
        age = self.get_age()
        return (f"ID: {self.id}, ФИО: {self.last_name} {self.first_name} {self.middle_name}, "
                f"Возраст: {age}, Должность: {self.position}, Зарплата: {self.salary}")



class EmployeeSystem:
    def __init__(self):
        self.employees = []
        self.next_id = 1

    def load_from_file(self, filename):
        """Загрузка данных из файла"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.employees = [Employee.from_dict(emp) for emp in data]
                if self.employees:
                    self.next_id = max(emp.id for emp in self.employees) + 1
            print(f"Данные успешно загружены из файла {filename}")
        except FileNotFoundError:
            print(f"Файл {filename} не найден. Создан новый список сотрудников.")
            self.employees = []
        except json.JSONDecodeError:
            print("Ошибка чтения файла. Создан пустой список сотрудников.")
            self.employees = []

    def save_to_file(self, filename):
        """Сохранение данных в файл"""
        try:
            data = [emp.to_dict() for emp in self.employees]
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            print(f"Данные успешно сохранены в файл {filename}")
        except Exception as e:
            print(f"Ошибка при сохранении в файл: {e}")

    def add_employee(self):
        """Добавление нового сотрудника"""
        print("\n--- Добавление нового сотрудника ---")
        last_name = input("Фамилия: ")
        first_name = input("Имя: ")
        middle_name = input("Отчество: ")

        while True:
            try:
                birth_year = int(input("Год рождения: "))
                break
            except ValueError:
                print("Пожалуйста, введите корректный год.")

        position = input("Должность: ")

        while True:
            try:
                salary = float(input("Зарплата: "))
                break
            except ValueError:
                print("Пожалуйста, введите корректную зарплату.")

        new_employee = Employee(self.next_id, last_name, first_name, middle_name, birth_year, position, salary)
        self.employees.append(new_employee)
        self.next_id += 1
        print(f"Сотрудник {last_name} успешно добавлен!")

    def edit_employee(self):
        """Редактирование сотрудника по ID"""
        if not self.employees:
            print("Список сотрудников пуст.")
            return

        try:
            emp_id = int(input("Введите ID сотрудника для редактирования: "))
            employee = next((emp for emp in self.employees if emp.id == emp_id), None)

            if employee:
                print(f"\nРедактирование сотрудника: {employee}")
                employee.last_name = input(f"Фамилия ({employee.last_name}): ") or employee.last_name
                employee.first_name = input(f"Имя ({employee.first_name}): ") or employee.first_name
                employee.middle_name = input(f"Отчество ({employee.middle_name}): ") or employee.middle_name

                while True:
                    birth_input = input(f"Год рождения ({employee.birth_year}): ")
                    if birth_input:
                        try:
                            employee.birth_year = int(birth_input)
                            break
                        except ValueError:
                            print("Пожалуйста, введите корректный год.")
                    else:
                        break

                employee.position = input(f"Должность ({employee.position}): ") or employee.position

                while True:
                    salary_input = input(f"Зарплата ({employee.salary}): ")
                    if salary_input:
                        try:
                            employee.salary = float(salary_input)
                            break
                        except ValueError:
                            print("Пожалуйста, введите корректную зарплату.")
                    else:
                        break

                print("Данные сотрудника успешно обновлены!")
            else:
                print("Сотрудник с таким ID не найден.")
        except ValueError:
            print("Некорректный ID.")

    def delete_employee(self):
        """Удаление сотрудника по ID"""
        if not self.employees:
            print("Список сотрудников пуст.")
            return

        try:
            emp_id = int(input("Введите ID сотрудника для удаления: "))
            employee = next((emp for emp in self.employees if emp.id == emp_id), None)

            if employee:
                self.employees.remove(employee)
                print(f"Сотрудник {employee.last_name} успешно удалён!")
            else:
                print("Сотрудник с таким ID не найден.")
        except ValueError:
            print("Некорректный ID.")

    def search_by_last_name(self):
        """Поиск сотрудника по фамилии"""
        search_name = input("Введите фамилию для поиска: ").lower()
        found = [emp for emp in self.employees if search_name in emp.last_name.lower()]

        if found:
            print(f"\nНайдено сотрудников: {len(found)}")
            for emp in found:
                print(emp)
            self.save_search_results(found, f"search_by_{search_name}")
        else:
            print("Сотрудники с такой фамилией не найдены.")

    def filter_by_age(self):
        """Вывод сотрудников указанного возраста"""
        try:
            age = int(input("Введите возраст для фильтрации: "))
            current_year = datetime.now().year
            birth_year = current_year - age
            found = [emp for emp in self.employees if emp.birth_year == birth_year]

            if found:
                print(f"\nСотрудники возраста {age} лет: {len(found)}")
                for emp in found:
                    print(emp)
                self.save_search_results(found, f"age_{age}")
            else:
                print(f"Сотрудники возраста {age} лет не найдены.")
        except ValueError:
            print("Пожалуйста, введите корректный возраст.")

    def filter_by_first_letter(self):
        """Вывод сотрудников, фамилия которых начинается на указанную букву"""
        letter = input("Введите первую букву фамилии: ").lower()
        found = [emp for emp in self.employees if emp.last_name.lower().startswith(letter)]

        if found:
            print(f"\nСотрудники, фамилия которых начинается на '{letter}': {len(found)}")
            for emp in found:
                print(emp)
            self.save_search_results(found, f"starts_with_{letter}")
        else:
            print(f"Сотрудники с фамилией на букву '{letter}' не найдены.")

    def display_all(self):
        """Вывод информации обо всех сотрудниках"""
        if not self.employees:
            print("Список сотрудников пуст.")
            return

        print(f"\n--- Все сотрудники ({len(self.employees)}): ---")
        for emp in self.employees:
            print(emp)

    def save_search_results(self, employees, filename_suffix):
        """Сохранение результатов поиска в файл"""
        if not employees:
            print("Нет данных для сохранения.")
            return

        filename = f"search_results_{filename_suffix}.json"
        try:
            data = [emp.to_dict() for emp in employees]
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            print(f"Результаты поиска сохранены в файл: {filename}")
        except Exception as e:
            print(f"Ошибка при сохранении результатов поиска: {e}")

    def show_menu(self):
        """Отображение меню системы"""
        print("\n" + "="*50)
        print("          ИНФОРМАЦИОННАЯ СИСТЕМА «СОТРУДНИКИ»")
        print("="*50)
        print("1. Добавить сотрудника")
        print("2. Редактировать сотрудника")
        print("3. Удалить сотрудника")
        print("4. Поиск сотрудника по фамилии")
        print("5. Вывести сотрудников указанного возраста")
        print("6. Вывести сотрудников по первой букве фамилии")
        print("7. Показать всех сотрудников")
        print("8. Сохранить данные в файл")
        print("9. Выход")
        print("-"*50)

    def run(self):
        """Основной цикл работы программы"""
        # Запрашиваем имя файла для загрузки данных
        filename = input("Введите имя файла для загрузки данных (или Enter для создания нового): ").strip()
        if filename:
            self.load_from_file(filename)
        else:
            print("Создан новый список сотрудников.")

        while True:
            self.show_menu()
            choice = input("Выберите пункт меню (1-9): ").strip()

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.edit_employee()
            elif choice == '3':
                self.delete_employee()
            elif choice == '4':
                self.search_by_last_name()
            elif choice == '5':
                self.filter_by_age()
            elif choice == '6':
                self.filter_by_first_letter()
            elif choice == '7':
                self.display_all()
            elif choice == '8':
                filename = input("Введите имя файла для сохранения: ").strip()
                if filename:
                    self.save_to_file(filename)
                else:
                    print("Имя файла не может быть пустым.")
            elif choice == '9':
                # Автоматическое сохранение перед выходом
                auto_save = input("Сохранить данные перед выходом? (y/n): ").strip().lower()
                if auto_save in ('y', 'yes', 'д', 'да'):
                    filename = input("Введите имя файла для сохранения: ").strip()
                    if filename:
                        self.save_to_file(filename)
                    else:
                        print("Данные не сохранены — имя файла пустое.")
                print("Выход из программы. До свидания!")
                break
            else:
                print("Неверный выбор. Пожалуйста, введите число от 1 до 9.")



# Основная часть программы
if __name__ == "__main__":
    system = EmployeeSystem()
    system.run()
