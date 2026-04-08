#Model

from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: int

class CartModel:
    def __init__(self):
        self.products= {
            'apple': Product('яблоко', 80),
            'banana': Product('банан', 60),
            'coffee': Product('кофе', 70)
        }
        self.items= []

    def add_item(self, product_code: str):
        if product_code not in self.products:
            raise ValueError('товара нет')
        self.items.append(self.products[product_code])

    def total(self):
        return sum(item.price for item in self.items)
    
    def item_names(self):
        return [item.name for item in self.items]
    
#View
    class ConsoleCartView:
        @staticmethod
        def render_cart(items, total):
            print('корзина')

            if items:
                for item in items:
                    print(f'{item}')

            else:
                print('-пусто')
            print(f'итого: {total}')

        @staticmethod
        def render_error(msg):
            print(f'ошибка: {msg}')


#Controller

class CartController:
    def __init__(self, model: CartModel, view: ConsoleCartView):
        self.model= model
        self.view= view

    def add_product(self, product_code):
        try:
            self.model.add_item(product_code)
            self.view.render_cart(self.model.item_names(), self.model.total())
        except ValueError as e:
            self.view.render_error(str(e))

controller= CartController(CartModel(), ConsoleCartView())