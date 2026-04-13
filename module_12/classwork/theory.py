## Паттерны

# Template Method

class ReportTemplate:
    def build(self):
        data = self.fetch_data()
        return self.format_data(data)
    
    def fetch_data(self):
        raise NotImplementedError
    
    def format_data(self):
        raise NotImplementedError
    
class SalesReport(ReportTemplate):
    def fetch_data(self):
        return [100,200,300]
    
    def format_data(self, data):
        return f'сумма продаж: {sum(data)}'
    
print(SalesReport().build())


# Visitor

class Book:
    def _init(self, title, price):
        self.title = title
        self.price = price

    def accept(self, visitor):
        return visitor.visit_book(self)
    
class Course:
    def _init(self, title, price):
        self.title = title
        self.price = price

    def accept(self, visitor):
        return visitor.visit_course(self)
    
class DiscountVisitor:
    def visit_book(self, book):
        return f'{book.title}: {book.price * 0.9}'
    
    def visit_cource(self, cource):
        return f'{cource.title}: {cource.price * 0.9}'
    
visitor = DiscountVisitor()
items= [Book('book', 1000), Course('cource', 5000)]
for item in items:
    print(item.accept(visitor))