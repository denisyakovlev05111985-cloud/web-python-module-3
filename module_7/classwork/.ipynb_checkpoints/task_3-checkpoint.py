lines = [
    "SHP-1001,North,Chicago,3,3,40,delivered",
    "SHP-1002,North,Boston,4,6,20,delivered",
    "SHP-1003,East,Miami,2,2,35,cancelled",
    "SHP-1004,East,Chicago,5,8,15,delivered",
    "SHP-1005,West,Dallas,1,1,50,delivered",
    "SHP-1006,West,Miami,2,4,30,delivered",
    "SHP-1002,North,Boston,4,6,20,delivered",
    "SHP-1007,South,Atlanta,6,6,25,in_transit",
    "SHP-1008,South,Dallas,3,5,10,delivered"
]

deliveries = []
# список словарей с записями доставок
# ключи: shipment_id, warehouse, city, planned_day, actual_day, items, status

warehouse_stats = {}
# warehouse -> {"total": 0, "delayed": 0}

cities = set()
# множество городов доставки

shipment_counter = {}
# shipment_id -> количество встреч

duplicate_shipments = []
# список shipment_id, которые дублируются

city_delivered_items = {}
# city -> суммарное количество items для status == delivered


with open("delivery_log.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line + '\n')

with open("delivery_log.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(',')
        shipment_id, warehouse, city = parts[0], parts[1], parts[2]
        planned_day = int(parts[3])
        actual_day = int(parts[4])
        items= int(parts[5])
        status = parts[6]

        deliveries.append({
            'shipment_id': shipment_id,
            'warehouse': warehouse,
            'city': city,
            'planned_day': planned_day,
            'actual_day': actual_day,
            'items': items,
            'status': status
        })


for delivery in deliveries:
    shipment_id, warehouse, city, planned_day, actual_day, items, status= delivery['shipment_id'], delivery['warehouse'], delivery['city'], delivery['planned_day'], delivery['actual_day'], delivery['items'], delivery['status']

    warehouse_stats.setdefault(warehouse, {"total": 0, "delayed": 0})
    warehouse_stats[warehouse]['total'] +=1
    if actual_day > planned_day:
        warehouse_stats[warehouse]['delayed'] +=1

    cities.add(city)
    
    shipment_counter[shipment_id] = shipment_counter.get(shipment_id, 0) + 1

    if status == 'delivered':
        city_delivered_items[city] = city_delivered_items.get(city, 0)
        city_delivered_items[city] += items

print(city_delivered_items,warehouse_stats)

for shipment_id, count in shipment_counter.items():
    if count > 1:
        duplicate_shipments.append(shipment_id)
print(duplicate_shipments)   

worst_warehouse = None
max_delay_rate = -1

for warehouse, rate in warehouse_stats.items():
    delayed = int(rate['delayed'])
    total = int(rate['total'])
    delay_rate = delayed/total
    if delay_rate > max_delay_rate:
        max_delay_rate = delay_rate
        worst_warehouse = warehouse

print(worst_warehouse, max_delay_rate)

with open("delivery_report.txt", "w", encoding="utf-8") as file:
    file.write('- статистика по складам\n')
    for key, value in warehouse_stats.items():
        file.write(f' {key}: {value}\n')
   file.write('- список городов\n')
   file.write(f' {key}: {value}\n')
   cities
   for key, value in total_action_exit.items():
      file.write(f' {key}: {value}\n')
#    file.write('находится ли человек ВНУТРИ... Да- True. Нет- False\n')
#    for key, value in inside.items():
#       file.write(f' {key}: {value}\n')
#    file.write(f'люди с ошибками доступа {errors}\n')
#    file.write(f'датa {max_day} с максимальным количеством входов {max_enters}\n')
   
    # TODO:
    # записать в отчет:
    # - статистику по складам
    # - список городов
    # - дубликаты shipment_id
    # - склад с максимальным процентом просрочек
    # - доставленные объёмы по городам
    pass
