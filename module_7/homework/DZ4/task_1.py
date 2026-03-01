# 1. Посчитать общее количество покупок каждого пользователя.

# 2. Посчитать общую сумму потраченных денег каждым пользователем.

# 3. Для каждого пользователя:
#    - найти множество уникальных товаров, которые он покупал
#    - посчитать общее количество купленных товаров (с учётом повторов)

# 4. Найти товар, который покупали чаще всего
#    (если таких несколько — можно вернуть любой).

# 5. Найти пользователя, который:
#    - потратил больше всего денег
#    - купил больше всего товаров
#    (это могут быть разные пользователи)




from collections import defaultdict, Counter
import datetime

def analyze_purchases(purchases):
    
    user_count = defaultdict(int)
    for purchase in purchases:
        user_count[purchase['user']] += 1
    
    
    total_spent = defaultdict(int)
    for purchase in purchases:
        total_spent[purchase['user']] += purchase['price']
    
    
    unique_items = defaultdict(set)
    total_items = defaultdict(int)
    for purchase in purchases:
        unique_items[purchase['user']].update(purchase['items'])
        total_items[purchase['user']] = len(purchase['items'])
    
   
    item_counts = defaultdict(int)
    for item in set(item for purchase in purchases for item in purchase['items']):
        for purchase in purchases:
            if item in purchase['items']:
                item_counts[item] += 1
                break
    most_common_item = max(item_counts, key=item_counts.get)
    
    
    max_spender = max(purchases, key=lambda x: x['price'])
    max_buyer = max(purchases, key=lambda x: len(x['items']))
    
    
    return {
        "user_count": user_count,
        "total_spent": total_spent,
        "unique_items": unique_items,
        "total_items": total_items,
        "most_common_item": most_common_item,
        "max_spender": max_spender,
        "max_buyer": max_buyer,
    }


purchases = [
    {"user": "Алиса", "items": ["яблоко", "банан"], "price": 120, "timestamp": 1},
    {"user": "Боб", "items": ["банан"], "price": 50, "timestamp": 2},
    {"user": "Алиса", "items": ["апельсин", "яблоко"], "price": 150, "timestamp": 5},
    {"user": "Боб", "items": ["яблоко", "апельсин"], "price": 130, "timestamp": 6},
    {"user": "Алиса", "items": ["банан", "банан"], "price": 70, "timestamp": 15},
    {"user": "Боб", "items": ["банан"], "price": 40, "timestamp": 25}
]

result = analyze_purchases(purchases)


print("1-Количество покупок: ", result["user_count"])
print("2-Общая сумма:", result["total_spent"])
print("3-Уникальные товары:", result["unique_items"])
print("4-Всего куплено:", result["total_items"])
print("5-Самый частый товар:", result["most_common_item"])
print("6-Больше всего потратил:", result["max_spender"])
print("7-Больше всего купил:", result["max_buyer"])
