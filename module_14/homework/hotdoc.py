from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime
from typing import List, Dict
import json
import os


# Константы
DISCOUNT_THRESHOLDS = {
    3: 0.1,  # 10% при заказе от 3 шт.
    5: 0.15  # 15% при заказе от 5 шт.
}
LOW_STOCK_THRESHOLD = 10  # Порог низкого запаса


class Ingredient:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def use(self, quantity: int = 1) -> bool:
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False

    def restock(self, quantity: int):
        self.stock += quantity

class ToppingType(Enum):
    MAYO_SAUCE = "Майонез"
    MUSTARD = "Горчица"
    KETCHUP = "Кетчуп"
    SWEET_ONION = "Сладкий лук"
    JALAPENO = "Халапеньо"
    CHILI = "Чили"
    PICKLED_CUCUMBER = "Солёный огурец"

class HotDogRecipe(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_base_price(self) -> float:
        pass

    @abstractmethod
    def get_ingredients(self) -> List[str]:
        pass

    @abstractmethod
    def get_cost_price(self) -> float:
        """Возвращает себестоимость рецепта"""
        pass

class StandardHotDogRecipe(HotDogRecipe):
    def __init__(self, name: str, base_price: float, ingredients: List[str], cost_price: float):
        self._name = name
        self._base_price = base_price
        self._ingredients = ingredients
        self._cost_price = cost_price

    def get_name(self) -> str:
        return self._name

    def get_base_price(self) -> float:
        return self._base_price

    def get_ingredients(self) -> List[str]:
        return self._ingredients.copy()

    def get_cost_price(self) -> float:
        return self._cost_price

class CustomHotDogRecipe(HotDogRecipe):
    def __init__(self, base_price: float = 50.0):
        self._name = "Собственный рецепт"
        self._base_price = base_price
        self._ingredients: List[str] = ["Булочка", "Сосиска"]
        self._toppings: List[ToppingType] = []
        self._topping_cost = 10.0  # Стоимость каждого топпинга

    def add_topping(self, topping: ToppingType):
        self._toppings.append(topping)
        self._ingredients.append(topping.value)

    def get_name(self) -> str:
        return self._name

    def get_base_price(self) -> float:
        base = self._base_price
        for topping in self._toppings:
            base += self._topping_cost
        return base

    def get_ingredients(self) -> List[str]:
        return self._ingredients.copy()

    def get_cost_price(self) -> float:
        # Упрощённый расчёт себестоимости для кастомного рецепта
        base_cost = 40.0  # Базовая себестоимость без топпингов
        topping_cost = len(self._toppings) * 5.0  # Себестоимость каждого топпинга — 5 руб.
        return base_cost + topping_cost

class HotDogFactory:
    _recipes = {
        "basic": StandardHotDogRecipe("Классический", 80.0, ["Булочка", "Сосиска", "Горчица"], 55.0),
        "spicy": StandardHotDogRecipe("Острый", 90.0, ["Булочка", "Сосиска", "Халапеньо", "Чили"], 60.0),
        "deluxe": StandardHotDogRecipe("Делюкс", 120.0, ["Булочка", "Сосиска", "Сладкий лук", "Солёный огурец", "Майонез"], 85.0)
    }

    @staticmethod
    def create_recipe(recipe_type: str) -> HotDogRecipe:
        if recipe_type in HotDogFactory._recipes:
            return HotDogFactory._recipes[recipe_type]
        elif recipe_type == "custom":
            return CustomHotDogRecipe()
        else:
            raise ValueError("Неизвестный тип рецепта")

class Inventory:
    def __init__(self):
        self.ingredients: Dict[str, Ingredient] = {
            "Булочка": Ingredient("Булочка", 10.0, 50),
            "Сосиска": Ingredient("Сосиска", 30.0, 40),
            "Майонез": Ingredient("Майонез", 5.0, 30),
            "Горчица": Ingredient("Горчица", 5.0, 30),
            "Кетчуп": Ingredient("Кетчуп", 5.0, 30),
            "Сладкий лук": Ingredient("Сладкий лук", 8.0, 20),
            "Халапеньо": Ingredient("Халапеньо", 15.0, 15),
            "Чили": Ingredient("Чили", 12.0, 15),
            "Солёный огурец": Ingredient("Солёный огурец", 10.0, 20)
        }
        self.observers: List[InventoryObserver] = []

    def register_observer(self, observer: 'InventoryObserver'):
        self.observers.append(observer)

    def notify_observers(self, low_stock_items: List[str]):
        for observer in self.observers:
            observer.update(low_stock_items)

    def check_and_notify_low_stock(self):
        low_stock = []
        for name, ingredient in self.ingredients.items():
            if ingredient.stock < LOW_STOCK_THRESHOLD:
                low_stock.append(f"{name} (осталось: {ingredient.stock})")
        if low_stock:
            self.notify_observers(low_stock)

    def use_ingredients(self, recipe: HotDogRecipe, quantity: int) -> bool:
        ingredients = recipe.get_ingredients()
        # Сначала проверяем, хватит ли всех ингредиентов
        for ingredient_name in ingredients:
            if ingredient_name not in self.ingredients:
                return False
            ingredient = self.ingredients[ingredient_name]
            if ingredient.stock < quantity:
                return False
        # Если проверка пройдена, используем ингредиенты
        for ingredient_name in ingredients:
            self.ingredients[ingredient_name].use(quantity)
        self.check_and_notify_low_stock()
        return True

class InventoryObserver(ABC):
    @abstractmethod
    def update(self, low_stock_items: List[str]):
        pass

class LowStockNotifier(InventoryObserver):
    def update(self, low_stock_items: List[str]):
        print("\n⚠️ ВНИМАНИЕ: Низкий запас ингредиентов!")
        for item in low_stock_items:
            print(f"  - {item}")
        print()

class SalesStatistics:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.total_hotdogs_sold = 0
            cls._instance.total_revenue = 0.0
            cls._instance.total_profit = 0.0
        return cls._instance

    def record_sale(self, hotdog: 'HotDog', payment_type: str):
        cost = hotdog.calculate_cost()
        cost_price = hotdog.recipe.get_cost_price() * hotdog.quantity
        self.total_hotdogs_sold += hotdog.quantity
        self.total_revenue += cost
        self.total_profit += (cost - cost_price)

    def get_report(self) -> Dict:
        return {
            "total_hotdogs_sold": self.total_hotdogs_sold,
            "total_revenue": round(self.total_revenue, 2),
            "total_profit": round(self.total_profit, 2)
        }

class HotDog:
    def __init__(self, recipe: HotDogRecipe, quantity: int = 1):
        self.recipe = recipe
        self.quantity = quantity
        self.order_time = datetime.now()

    def calculate_cost(self) -> float:
        base_price = self.recipe.get_base_price()
        total = base_price * self.quantity

        # Применяем скидку при заказе от 3 хот‑догов
        discount = 0.0
        for threshold, discount_rate in sorted(DISCOUNT_THRESHOLDS.items(), reverse=True):
            if self.quantity >= threshold:
                discount = discount_rate
                break

        return round(total * (1 - discount), 2)

    def to_dict(self) -> Dict:
        return {
            "recipe_name": self.recipe.get_name(),
            "quantity": self.quantity,
            "ingredients": self.recipe.get_ingredients(),
            "cost": self.calculate_cost(),
            "order_time": self.order_time.strftime("%Y-%m-%d %H:%M:%S")
        }

    def display_info(self):
        print(f"\n🌭 Заказ хот‑дога:")
        print(f"Рецепт: {self.recipe.get_name()}")
        print(f"Количество: {self.quantity} шт.")
        print(f"Ингредиенты: {', '.join(self.recipe.get_ingredients())}")
        print(f"Стоимость: {self.calculate_cost()} руб.")

        if self.quantity >= 3:
            discount_applied = 0.0
            for threshold, rate in sorted(DISCOUNT_THRESHOLDS.items(), reverse=True):
                if self.quantity >= threshold:
                    discount_applied = rate
                    break
            if discount_applied > 0:
                print(f"(применена скидка {discount_applied * 100}% за объём)")
        print()

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class CashPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Оплата наличными: {amount} руб.")
        return True

class CardPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Оплата картой: {amount} руб.")
        # Здесь может быть интеграция с платёжным шлюзом
        return True

class PaymentFactory:
    @staticmethod
    def create_processor(payment_type: str) -> PaymentProcessor:
        if payment_type == "cash":
            return CashPayment()
        elif payment_type == "card":
            return CardPayment()
        else:
            raise ValueError("Неизвестный тип оплаты")

class OrderManager:
    def __init__(self, inventory: Inventory, statistics: SalesStatistics):
        self.inventory = inventory
        self.statistics = statistics
        self.orders: List[HotDog] = []

    def place_order(self, hotdog: HotDog, payment_type: str) -> bool:
        # Проверяем наличие ингредиентов
        if not self.inventory.use_ingredients(hotdog.recipe, hotdog.quantity):
            print("❌ Недостаточно ингредиентов для приготовления хот‑дога!")
            return False

        # Обрабатываем оплату
        processor = PaymentFactory.create_processor(payment_type)
        if not processor.process_payment(hotdog.calculate_cost()):
            print("❌ Ошибка при обработке платежа!")
            return False

        # Фиксируем продажу
        self.statistics.record_sale(hotdog, payment_type)
        self.orders.append(hotdog)

        # Сохраняем заказ в файл
        self._save_order_to_file(hotdog)
        return True

    def _save_order_to_file(self, hotdog: HotDog):
        order_data = hotdog.to_dict()
        try:
            with open("orders.json", "a", encoding="utf-8") as f:
                f.write(json.dumps(order_data, ensure_ascii=False) + "\n")
        except Exception as e:
            print(f"Ошибка при сохранении заказа: {e}")

    def get_order_history(self) -> List[Dict]:
        orders = []
        try:
            with open("orders.json", "r", encoding="utf-8") as f:
                for line in f:
                    orders.append(json.loads(line))
        except FileNotFoundError:
            pass
        return orders

class HotDogKiosk:
    def __init__(self):
        self.inventory = Inventory()
        self.statistics = SalesStatistics()
        self.order_manager = OrderManager(self.inventory, self.statistics)

        # Подключаем уведомления о низком запасе
        notifier = LowStockNotifier()
        self.inventory.register_observer(notifier)

    def run(self):
        while True:
            self.show_main_menu()
            choice = input("Выберите действие: ").strip()

            if choice == "1":
                self.create_order()
            elif choice == "2":
                self.show_sales_report()
            elif choice == "3":
                self.show_inventory_status()
            elif choice == "4":
                print("Выход из программы...")
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    def show_main_menu(self):
        print("\n" + "="*50)
        print("🌭 КИОСК ПО ПРОДАЖЕ ХОТ‑ДОГОВ")
        print("="*50)
        print("1. Создать заказ")
        print("2. Показать статистику продаж")
        print("3. Показать статус запасов")
        print("4. Выход")
        print("-"*50)

    def create_order(self):
        print("\n🛒 СОЗДАНИЕ ЗАКАЗА")
        print("Доступные рецепты:")
        print("1. Классический (80 руб.)")
        print("2. Острый (90 руб.)")
        print("3. Делюкс (120 руб.)")
        print("4. Собственный рецепт")

        choice = input("Выберите рецепт (1–4): ").strip()
        recipe = None

        try:
            if choice == "1":
                recipe = HotDogFactory.create_recipe("basic")
            elif choice == "2":
                recipe = HotDogFactory.create_recipe("spicy")
            elif choice == "3":
                recipe = HotDogFactory.create_recipe("deluxe")
            elif choice == "4":
                recipe = HotDogFactory.create_recipe("custom")
                self._configure_custom_recipe(recipe)
            else:
                print("Неверный выбор рецепта")
                return

            # Ввод количества с обработкой ошибок
            while True:
                try:
                    quantity_input = input("Количество хот‑догов: ").strip()
                    quantity = int(quantity_input)
                    if quantity <= 0:
                        print("Количество должно быть положительным числом.")
                        continue
                    break
                except ValueError:
                    print("Пожалуйста, введите корректное число.")

            hotdog = HotDog(recipe, quantity)
            hotdog.display_info()

            payment_choice = input("Способ оплаты (1 — наличные, 2 — карта): ").strip()
            payment_type = "cash" if payment_choice == "1" else "card"

            if self.order_manager.place_order(hotdog, payment_type):
                print("✅ Заказ успешно оформлен!")
            else:
                print("❌ Заказ не может быть выполнен")

        except ValueError as e:
            print(f"Ошибка: {e}")

    def _configure_custom_recipe(self, recipe: CustomHotDogRecipe):
        print("Настройка собственного рецепта:")
        for topping in ToppingType:
            while True:
                add = input(f"Добавить {topping.value}? (y/n): ").strip().lower()
                if add in ('y', 'n'):
                    break
                print("Пожалуйста, введите 'y' или 'n'.")
            if add == 'y':
                recipe.add_topping(topping)

    def show_sales_report(self):
        report = self.statistics.get_report()
        print("\n📊 СТАТИСТИКА ПРОДАЖ")
        print(f"Всего продано хот‑догов: {report['total_hotdogs_sold']}")
        print(f"Общая выручка: {report['total_revenue']} руб.")
        print(f"Общая прибыль: {report['total_profit']} руб.")

    def show_inventory_status(self):
        print("\n📦 СТАТУС ЗАПАСОВ")
        for name, ingredient in self.inventory.ingredients.items():
            status = "⚠️ Низкий запас" if ingredient.stock < LOW_STOCK_THRESHOLD else "✅ В норме"
            print(f"{name}: {ingredient.stock} шт. — {status}")


if __name__ == "__main__":
    kiosk = HotDogKiosk()
    kiosk.run()
