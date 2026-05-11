import json
import os
from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic

# === ENTITIES ===

class Material:
    def __init__(self, material_id: int, name: str, category: str,
                 unit: str, quantity: int, min_quantity: int):
        self.id = material_id
        self.name = name
        self.category = category
        self.unit = unit
        self.quantity = quantity
        self.min_quantity = min_quantity

    def needs_replenishment(self) -> bool:
        return self.quantity <= self.min_quantity

class Request:
    def __init__(self, request_id: int, employee_name: str, department: str,
                 material_id: int, quantity: int, reason: str, status: str):
        self.id = request_id
        self.employee_name = employee_name
        self.department = department
        self.material_id = material_id
        self.quantity = quantity
        self.reason = reason
        self.status = status

    VALID_STATUSES = ["новая", "одобрена", "отклонена", "выполнена"]

    def is_valid_status(self, status: str) -> bool:
        return status in self.VALID_STATUSES

    def can_be_written_off(self) -> bool:
        return self.status == "одобрена"

# === REPOSITORIES ===

T = TypeVar('T')

class BaseRepository(ABC, Generic[T]):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def add(self, item: T):
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def find_by_id(self, item_id: int) -> Optional[T]:
        pass

    @abstractmethod
    def update(self, item: T):
        pass

class MaterialRepository(BaseRepository[Material]):
    def __init__(self, filename: str = "materials.json"):
        self.filename = filename
        self._materials: List[Material] = []
        self._next_id = 1
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self._materials = [
                    Material(**item) for item in data
                ]
                if self._materials:
                    self._next_id = max(m.id for m in self._materials) + 1

    def save(self):
        data = [
            {
                'id': m.id,
                'name': m.name,
                'category': m.category,
                'unit': m.unit,
                'quantity': m.quantity,
                'min_quantity': m.min_quantity
            }
            for m in self._materials
        ]
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add(self, material: Material):
        material.id = self._next_id
        self._next_id += 1
        self._materials.append(material)

    def get_all(self) -> List[Material]:
        return self._materials.copy()

    def find_by_id(self, material_id: int) -> Optional[Material]:
        for material in self._materials:
            if material.id == material_id:
                return material
        return None

    def update(self, material: Material):
        for i, m in enumerate(self._materials):
            if m.id == material.id:
                self._materials[i] = material
                break

class RequestRepository(BaseRepository[Request]):
    def __init__(self, filename: str = "requests.json"):
        self.filename = filename
        self._requests: List[Request] = []
        self._next_id = 1
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self._requests = [
                    Request(**item) for item in data
                ]
                if self._requests:
                    self._next_id = max(r.id for r in self._requests) + 1

    def save(self):
        data = [
            {
                'id': r.id,
                'employee_name': r.employee_name,
                'department': r.department,
                'material_id': r.material_id,
                'quantity': r.quantity,
                'reason': r.reason,
                'status': r.status
            }
            for r in self._requests
        ]
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add(self, request: Request):
        request.id = self._next_id
        self._next_id += 1
        self._requests.append(request)

    def get_all(self) -> List[Request]:
        return self._requests.copy()

    def find_by_id(self, request_id: int) -> Optional[Request]:
        for request in self._requests:
            if request.id == request_id:
                return request
        return None

    def update(self, request: Request):
        for i, r in enumerate(self._requests):
            if r.id == request.id:
                self._requests[i] = request
                break

    def find_by_criteria(self, warehouse_service, **criteria) -> List[Request]:
        results = []
        for request in self._requests:
            match = True
            for key, value in criteria.items():
                if key == 'employee_name' and value.lower() not in request.employee_name.lower():
                    match = False
                    break
                elif key == 'department' and value.lower() not in request.department.lower():
                    match = False
                    break
                elif key == 'status' and value.lower() != request.status.lower():
                    match = False
                    break
                elif key == 'material_name':
                    material = warehouse_service.material_repo.find_by_id(request.material_id)
                    if not material or value.lower() not in material.name.lower():
                        match = False
                break
            if match:
                results.append(request)
        return results

# === SERVICES ===

class WarehouseService:
    def __init__(self, material_repo: MaterialRepository, request_repo: RequestRepository):
        self.material_repo = material_repo
        self.request_repo = request_repo

    def add_material(self, name: str, category: str, unit: str,
                 quantity: int, min_quantity: int) -> Material:
        if quantity < 0:
            raise ValueError("Количество материала не может быть отрицательным.")
        if min_quantity < 0:
            raise ValueError("Минимальный остаток не может быть отрицательным.")

        material = Material(0, name, category, unit, quantity, min_quantity)             
        self.material_repo.add(material)
        return material

    def create_request(self, employee_name: str, department: str, material_id: int,
                  quantity: int, reason: str, status: str) -> Request:
        if status not in Request.VALID_STATUSES:
            raise ValueError(f"Недопустимый статус заявки. Допустимые значения: {', '.join(Request.VALID_STATUSES)}")
        material = self.material_repo.find_by_id(material_id)
        if not material:
            raise ValueError("Материал с указанным номером не найден.")
        if quantity <= 0:
            raise ValueError("Количество в заявке должно быть больше нуля.")
        if quantity > material.quantity:
            raise ValueError("Запрашиваемое количество превышает остаток на складе.")

        request = Request(0, employee_name, department, material_id, quantity, reason, status)
        self.request_repo.add(request)
        return request

    def change_request_status(self, request_id: int, new_status: str):
        if new_status not in Request.VALID_STATUSES:
            raise ValueError("Недопустимый статус заявки.")

        request = self.request_repo.find_by_id(request_id)
        if not request:
            raise ValueError("Заявка с указанным номером не найдена.")

        request.status = new_status
        self.request_repo.update(request)

    def replenish_material(self, material_id: int, quantity: int):
        if quantity <= 0:
            raise ValueError("Количество для пополнения должно быть больше нуля.")
        if quantity > 1_000_000:  # Защита от ввода чрезмерно больших чисел
            raise ValueError("Слишком большое количество для пополнения.")

        material = self.material_repo.find_by_id(material_id)
        if not material:
            raise ValueError("Материал с указанным номером не найден.")

        material.quantity += quantity
        self.material_repo.update(material)

    def write_off_material(self, request_id: int):
        request = self.request_repo.find_by_id(request_id)
        if not request:
            raise ValueError("Заявка с указанным номером не найдена.")

        if request.status == "выполнена":
            raise ValueError("Заявка уже выполнена, повторное списание невозможно.")

        if not request.can_be_written_off():
            raise ValueError("Списание возможно только по одобренной заявке.")

        material = self.material_repo.find_by_id(request.material_id)
        if not material:
            raise ValueError("Связанный материал не найден.")

        if material.quantity < request.quantity:
            raise ValueError("Недостаточно материала на складе.")

        # Выполняем списание
        material.quantity -= request.quantity
        request.status = "выполнена"

        self.material_repo.update(material)
        self.request_repo.update(request)

    def find_requests(self, **criteria) -> List[Request]:
        return self.request_repo.find_by_criteria(self, **criteria)

class StatisticsService:
    def __init__(self, material_repo: MaterialRepository, request_repo: RequestRepository):
        self.material_repo = material_repo
        self.request_repo = request_repo

    def get_statistics(self) -> dict:
        materials = self.material_repo.get_all()
        requests = self.request_repo.get_all()

        new_requests = sum(1 for r in requests if r.status == "новая")
        approved_requests = sum(1 for r in requests if r.status == "одобрена")
        rejected_requests = sum(1 for r in requests if r.status == "отклонена")
        completed_requests = sum(1 for r in requests if r.status == "выполнена")

        low_stock_materials = sum(1 for m in materials if m.needs_replenishment())
        total_units = sum(m.quantity for m in materials)

        return {
            'total_materials': len(materials),
            'total_requests': len(requests),
            'new_requests': new_requests,
            'approved_requests': approved_requests,
            'rejected_requests': rejected_requests,
            'completed_requests': completed_requests,
            'low_stock_materials': low_stock_materials,
            'total_units': total_units
        }

# === UI ===

class ConsoleUI:
    def __init__(self, warehouse_service: WarehouseService, statistics_service: StatisticsService):
        self.warehouse_service = warehouse_service
        self.statistics_service = statistics_service

    def show_menu(self):
        print("\n=== WarehouseRequest Console ===")
        print("1. Добавить материал на склад")
        print("2. Показать все материалы")
        print("3. Создать заявку на выдачу")
        print("4. Показать все заявки")
        print("5. Найти заявку")
        print("6. Изменить статус заявки")
        print("7. Пополнить остаток материала")
        print("8. Списать материал по заявке")
        print("9. Показать статистику")
        print("10. Сохранить данные")
        print("0. Выход")

    def run(self):
        while True:
            self.show_menu()
            choice = input("\nВыберите действие (0-10): ").strip()

            try:
                if choice == '1':
                    self._add_material()
                elif choice == '2':
                    self._show_materials()
                elif choice == '3':
                    self._create_request()
                elif choice == '4':
                    self._show_requests()
                elif choice == '5':
                    self._find_requests()
                elif choice == '6':
                    self._change_request_status()
                elif choice == '7':
                    self._replenish_material()
                elif choice == '8':
                    self._write_off_material()
                elif choice == '9':
                    self._show_statistics()
                elif choice == '10':
                    self._save_data()
                    print("Данные успешно сохранены.")
                elif choice == '0':
                    self._save_data()
                    print("Программа завершена. До свидания!")
                    break
                else:
                    print("Некорректный выбор. Попробуйте снова.")
            except ValueError as e:
                print(f"Ошибка ввода: {e}")
            except KeyboardInterrupt:
                print("\nПрограмма прервана пользователем. До свидания!")
                break
            except Exception as e:
                print(f"Неожиданная ошибка: {e}")


    def _add_material(self):
        print("\n--- Добавление материала ---")
        name = input("Название материала: ").strip()
        category = input("Категория материала: ").strip()
        unit = input("Единица измерения: ").strip()

        quantity = self._get_positive_int("Количество на складе: ", "Количество материала не может быть отрицательным.")
        min_quantity = self._get_positive_int("Минимальный остаток: ", "Минимальный остаток не может быть отрицательным.")

        try:
            material = self.warehouse_service.add_material(name, category, unit, quantity, min_quantity)
            print(f"Материал '{name}' успешно добавлен с номером {material.id}.")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def _show_materials(self):
        materials = self.warehouse_service.material_repo.get_all()
        if not materials:
            print("Материалы отсутствуют.")
            return

        for material in materials:
            print(f"\nНомер материала: {material.id}")
            print(f"Название: {material.name}")
            print(f"Категория: {material.category}")
            print(f"Единица измерения: {material.unit}")
            print(f"Количество на складе: {material.quantity}")
            print(f"Минимальный остаток: {material.min_quantity}")

            if material.needs_replenishment():
                print("Статус остатка: Требуется пополнение")

    def _create_request(self):
        print("\n--- Создание заявки на выдачу ---")
        employee_name = input("ФИО сотрудника: ").strip()
        department = input("Отдел сотрудника: ").strip()

        material_id = self._get_int("Номер материала: ")
        quantity = self._get_positive_int("Количество материала: ", "Количество в заявке должно быть больше нуля.")
        reason = input("Причина выдачи: ").strip()


        print("\nВыберите статус заявки:")
        for i, status in enumerate(Request.VALID_STATUSES, 1):
            print(f"{i}. {status}")
        status_choice = input(f"Введите номер статуса (1-{len(Request.VALID_STATUSES)}): ").strip()
        try:
            status_index = int(status_choice) - 1
            if 0 <= status_index < len(Request.VALID_STATUSES):
                status = Request.VALID_STATUSES[status_index]
            else:
                raise ValueError
        except ValueError:
            print("Некорректный выбор статуса. Заявка будет создана со статусом 'новая'.")
            status = "новая"

        try:
            request = self.warehouse_service.create_request(employee_name, department, material_id, quantity, reason, status)
            print(f"Заявка успешно создана с номером {request.id} со статусом '{request.status}'.")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def _show_requests(self):
        requests = self.warehouse_service.request_repo.get_all()
        if not requests:
            print("Заявки отсутствуют.")
            return

        for request in requests:
            material = self.warehouse_service.material_repo.find_by_id(request.material_id)
            material_name = material.name if material else "Неизвестный материал"
            material_unit = material.unit if material else ""

            print(f"\nНомер заявки: {request.id}")
            print(f"Сотрудник: {request.employee_name}")
            print(f"Отдел: {request.department}")
            print(f"Материал: {material_name}")
            print(f"Количество: {request.quantity} {material_unit}")
            print(f"Причина выдачи: {request.reason}")
            print(f"Статус: {request.status}")

    def _find_requests(self):
        print("\n--- Поиск заявок ---")
        print("1. Поиск по сотруднику")
        print("2. Поиск по отделу")
        print("3. Поиск по статусу")
        print("4. Поиск по названию материала")

        choice = input("Выберите критерий поиска (1-4): ").strip()
        search_term = input("Введите значение для поиска: ").strip().lower()

        if not search_term:
            print("Строка поиска не может быть пустой.")
            return

        criteria = {}
        if choice == '1':
            criteria['employee_name'] = search_term
        elif choice == '2':
            criteria['department'] = search_term
        elif choice == '3':
            criteria['status'] = search_term
        elif choice == '4':
            criteria['material_name'] = search_term
        else:
            print("Некорректный выбор критерия поиска.")
            return

        try:
            found_requests = self.warehouse_service.find_requests(**criteria)
            if not found_requests:
                print("Заявки не найдены.")
                return

            for request in found_requests:
                material = self.warehouse_service.material_repo.find_by_id(request.material_id)
                material_name = material.name if material else "Неизвестный материал"
                material_unit = material.unit if material else ""

                print(f"\nНомер заявки: {request.id}")
                print(f"Сотрудник: {request.employee_name}")
                print(f"Отдел: {request.department}")
                print(f"Материал: {material_name}")
                print(f"Количество: {request.quantity} {material_unit}")
                print(f"Причина выдачи: {request.reason}")
                print(f"Статус: {request.status}")
        except Exception as e:
            print(f"Ошибка при поиске заявок: {e}")

    def _change_request_status(self):
        request_id = self._get_int("Введите номер заявки: ")

        print("\nВыберите новый статус:")
        print("1. новая")
        print("2. одобрена")
        print("3. отклонена")
        print("4. выполнена")

        status_choice = input("Введите номер статуса (1-4): ").strip()
        status_map = {
            '1': "новая",
            '2': "одобрена",
            '3': "отклонена",
            '4': "выполнена"
        }

        new_status = status_map.get(status_choice)
        if not new_status:
            print("Недопустимый статус. Попробуйте снова.")
            return

        try:
            self.warehouse_service.change_request_status(request_id, new_status)
            print("Статус заявки успешно изменён.")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def _replenish_material(self):
        material_id = self._get_int("Введите номер материала: ")
        quantity = self._get_positive_int("Количество для добавления: ", "Количество для пополнения должно быть больше нуля.")

        try:
            self.warehouse_service.replenish_material(material_id, quantity)
            print("Остаток материала успешно пополнен.")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def _write_off_material(self):
        request_id = self._get_int("Введите номер заявки: ")

        try:
            self.warehouse_service.write_off_material(request_id)
            print("Материал успешно списан по заявке.")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def _show_statistics(self):
        try:
            stats = self.statistics_service.get_statistics()
            print("\n=== Статистика ===")
            print(f"Всего материалов: {stats['total_materials']}")
            print(f"Всего заявок: {stats['total_requests']}")
            print(f"Новые заявки: {stats['new_requests']}")
            print(f"Одобренные заявки: {stats['approved_requests']}")
            print(f"Отклоненные заявки: {stats['rejected_requests']}")
            print(f"Выполненные заявки: {stats['completed_requests']}")
            print(f"Материалы, требующие пополнения: {stats['low_stock_materials']}")
            print(f"Всего единиц материалов на складе: {stats['total_units']}")
        except Exception as e:
            print(f"Ошибка при получении статистики: {e}")

    def _save_data(self):
        try:
            self.warehouse_service.material_repo.save()
            self.warehouse_service.request_repo.save()
            print("Данные успешно сохранены.")
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")

    def _get_int(self, prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Пожалуйста, введите корректное целое число.")
            except KeyboardInterrupt:
                print("\nПрограмма прервана пользователем.")
                raise SystemExit

    def _get_positive_int(self, prompt: str, error_msg: str) -> int:
        while True:
            try:
                value = int(input(prompt))
                if value <= 0:
                    print(error_msg)
                    continue
                return value
            except ValueError:
                print("Пожалуйста, введите корректное целое число.")
            except KeyboardInterrupt:
                print("\nПрограмма прервана пользователем.")
                raise SystemExit

# === MAIN ===

def main():
    # Инициализация репозиториев
    material_repo = MaterialRepository()
    request_repo = RequestRepository()

    # Инициализация сервисов
    warehouse_service = WarehouseService(material_repo, request_repo)
    statistics_service = StatisticsService(material_repo, request_repo)

    # Запуск интерфейса
    ui = ConsoleUI(warehouse_service, statistics_service)
    print("Добро пожаловать в WarehouseRequest Console!")
    ui.run()

if __name__ == "__main__":
    main()
