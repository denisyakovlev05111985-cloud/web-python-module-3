rows = [
    'S-100,Acme,12.5,express,RU',
    'S-101,Beta,0,standard,RU',
    'S-102,Acme,abc,vip,KZ',
    'S-103,Delta,8.5,urgent,BY',
    'S-104,Gamma,15,vip,UZ',
    'S-105,Acme,4.0,standard,KZ',
    'S-106,Beta,9.5,express,BY',
]

class ShipmentError(Exception):
    pass

class RowFormatError(ShipmentError):
    pass

class WeightError(ShipmentError):
    pass

class PriorityError(ShipmentError):
    pass

class RegionError(ShipmentError):
    pass

def parse_shipment(row):
    try:
        parts = row.split(',')
        if len(parts) != 5:
            raise RowFormatError(f"Некорректный формат строки: {len(parts)}")

        shipment_id, client, weight_str, priority, region = parts

        try:
            weight = float(weight_str)
            if weight <= 0:
                raise WeightError(f"Вес должен быть больше 0: {weight}")
        except ValueError as e:
            raise WeightError(f"Некорректное значение веса: '{weight_str}'") from e

        valid_priorities = {'standard', 'express', 'vip'}
        if priority not in valid_priorities:
            raise PriorityError(f"Недопустимый приоритет: '{priority}'. Допустимые: {valid_priorities}")

        valid_regions = {'RU', 'KZ', 'BY'}
        if region not in valid_regions:
            raise RegionError(f"Недопустимый регион: '{region}'. Допустимые: {valid_regions}")

        return {
            'id': shipment_id,
            'client': client,
            'weight': weight,
            'priority': priority,
            'region': region
        }

    except ShipmentError:
        raise
    except Exception as e:
        raise RowFormatError(f"ошибка при парсинге строки: {e}") from e

def load_shipments(rows):
    shipments = []
    errors = []

    for row in rows:
        try:
            shipment = parse_shipment(row)
            shipments.append(shipment)
        except ShipmentError as e:
            errors.append((row, type(e).__name__, str(e)))

    return shipments, errors

if __name__ == "__main__":
    shipments, errors = load_shipments(rows)

    print(f"Валидных отгрузок: {len(shipments)}")
    print(f"Ошибок: {len(errors)}")

    error_counts = {}
    for error in errors:
        error_type = error[1]
        error_counts[error_type] = error_counts.get(error_type, 0) + 1

    print("\nОшибки по типам:")
    for error_type, count in error_counts.items():
        print(f"  {error_type}: {count}")

    premium_weight = sum(
        shipment['weight']
        for shipment in shipments
        if shipment['priority'] in {'express', 'vip'}
    )
    print(f"\nPremium weight (express/vip): {premium_weight}")

    client_weights = {}
    for shipment in shipments:
        client = shipment['client']
        client_weights[client] = client_weights.get(client, 0) + shipment['weight']

    if client_weights:
        leader_client = max(client_weights, key=client_weights.get)
        leader_weight = client_weights[leader_client]
        print(f"\nКлиент-лидер по суммарному весу: {leader_client} ({leader_weight})")
    else:
        print("\nНет валидных отгрузок для определения лидера.")
