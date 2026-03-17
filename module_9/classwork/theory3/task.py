# rows: sub_id|client_name|plan|visits_left|status
rows = [
    'SB-100|Alice|standard|8|active',
    'SB-101|Bob|premium|12|frozen',
    'SB-102|Charlie|family|0|expired',
    'SB-103|Diana|standard|5|active',
]

class Subscription:
    allowed_plans = {'standard', 'premium', 'family'}
    allowed_statuses = {'active', 'frozen', 'expired'}

    def __init__(self, sub_id, client_name, plan, visits_left, status):
        # TODO: сохранить sub_id, client_name, plan
        self.sub_id = sub_id
        self.client_name = client_name
        self.plan = plan
        # TODO: visits_left хранить через self._visits_left
        # TODO: значение visits_left пропустить через property/setter
        self.visits_left = visits_left  # используем сеттер
        # TODO: проверить plan и status, иначе raise ValueError
        if plan not in self.allowed_plans:
            raise ValueError(f"Недопустимый тариф: {plan}")
        if status not in self.allowed_statuses:
            raise ValueError(f"Недопустимый статус: {status}")
        self._status = status

    @property
    def visits_left(self):
        # TODO: вернуть текущее число посещений
        return self._visits_left

    @visits_left.setter
    def visits_left(self, value):
        # TODO: привести value к int
        value = int(value)
        # TODO: если value < 0 -> raise ValueError('Visits must be >= 0')
        if value < 0:
            raise ValueError('Visits must be >= 0')
        # TODO: сохранить результат в self._visits_left
        self._visits_left = value

    def use_visit(self):
        # TODO: если статус не 'active' -> raise ValueError
        if self._status != 'active':
            raise ValueError(f"Нельзя списать посещение: статус '{self._status}'")
        # TODO: если visits_left == 0 -> raise ValueError
        if self.visits_left == 0:
            raise ValueError("Нет доступных посещений")
        # TODO: уменьшить visits_left на 1
        self.visits_left -= 1
        # TODO: если после списания visits_left == 0, перевести статус в 'expired'
        if self.visits_left == 0:
            self._status = 'expired'

    def freeze(self):
        # TODO: если статус 'expired' -> raise ValueError
        if self._status == 'expired':
            raise ValueError("Нельзя заморозить истёкший абонемент")
        # TODO: перевести абонемент в 'frozen'
        self._status = 'frozen'

    def activate(self):
        # TODO: если visits_left == 0 -> raise ValueError
        if self.visits_left == 0:
            raise ValueError("Нельзя активировать абонемент без посещений")
        # TODO: перевести абонемент в 'active'
        self._status = 'active'

    @classmethod
    def from_row(cls, row):
        # TODO: split по '|'
        # TODO: ожидать 5 частей: sub_id, client_name, plan, visits_left, status
        parts = row.split('|')
        if len(parts) != 5:
            raise ValueError(f"Неверный формат строки: {row}")
        sub_id, client_name, plan, visits_left_raw, status = parts
        # TODO: вернуть Subscription(...)
        return cls(sub_id, client_name, plan, visits_left_raw, status)

    def __repr__(self):
        # TODO: вернуть строку вида Subscription(sub_id='...', client_name='...', status='...')
        return f"Subscription(sub_id='{self.sub_id}', client_name='{self.client_name}', status='{self._status}')"

class SubscriptionRegistry:
    def __init__(self):
        self.items = []

    def add(self, subscription):
        # TODO: добавить subscription в self.items
        self.items.append(subscription)

    def load(self, rows):
        # TODO: для каждой строки создать Subscription.from_row(row)
        # TODO: добавить объект в реестр через add(...)
        for row in rows:
            subscription = Subscription.from_row(row)
            self.add(subscription)

    def active_subscriptions(self):
        # TODO: вернуть список абонементов со статусом 'active'
        return [sub for sub in self.items if sub._status == 'active']

    def by_plan(self, plan):
        # TODO: вернуть список абонементов нужного тарифа
        return [sub for sub in self.items if sub.plan == plan]

    def total_visits_left(self):
        # TODO: вернуть суммарное число оставшихся посещений
        return sum(sub.visits_left for sub in self.items)

    def status_summary(self):
        # TODO: собрать dict вида status -> count
        summary = {}
        for sub in self.items:
            summary[sub._status] = summary.get(sub._status, 0) + 1
        return summary

    def find(self, sub_id):
        # TODO: вернуть абонемент по sub_id или None
        for sub in self.items:
            if sub.sub_id == sub_id:
                return sub
        return None

registry = SubscriptionRegistry()

# TODO: загрузить rows в registry
registry.load(rows)

# TODO: вывести все абонементы
print("Все абонементы:")
for sub in registry.items:
    print(f"  {sub}")

# TODO: вывести active_subscriptions()
print("\nАктивные абонементы:")
for sub in registry.active_subscriptions():
    print(f"  {sub}")

# TODO: вывести by_plan('standard')
print("\nАбонементы тарифа 'standard':")
for sub in registry.by_plan('standard'):
    print(f"  {sub}")

# TODO: вывести total_visits_left()
print(f"\nОбщее количество оставшихся посещений: {registry.total_visits_left()}")

# TODO: вывести status_summary()
print(f"Сводка по статусам: {registry.status_summary()}")

# TODO: найти абонемент 'SB-101', активировать его и вывести status_summary()
sub_101 = registry.find('SB-101')
if sub_101:
    sub_101.activate()
    print(f"\nПосле активации абонемента SB-101 сводка по статусам: {registry.status_summary()}")

# TODO: найти абонемент 'SB-100', списать одно посещение и вывести объект
sub_100 = registry.find('SB-100')
if sub_100:
    sub_100.use_visit()
    print(f"\nАбонемент SB-100 после списания посещения: {sub_100}")

