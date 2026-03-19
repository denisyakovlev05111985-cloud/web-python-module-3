# incident_id|service|severity|duration_min|channel|acknowledged
rows = [
    'INC-100|checkout|critical|12|pager|yes',
    'INC-101|search|high|7|slack|no',
    'INC-102|billing|medium|zero|email|yes',
    'INC-103|video|critical|-3|pager|no',
    'INC-104|feed|warning|5|slack|yes',
    'INC-105|auth|low|2|sms|no',
    'INC-106|cdn|high|4|email|maybe',
    'INC-107|ml|medium|9|slack|no',
]


class IncidentProcessingError(Exception):
    pass

class IncidentFormatError(IncidentProcessingError):
    pass

class SeverityError(IncidentProcessingError):
    pass

class DurationError(IncidentProcessingError):
    pass

class ChannelError(IncidentProcessingError):
    pass

class AcknowledgedFlagError(IncidentProcessingError):
    pass

def parse_incident(row):
    # TODO: split строку по '|'
    parts = row.split('|')
    # TODO: убрать лишние пробелы у частей через strip()
    parts = [part.strip() for part in parts]
    # TODO: ожидать 6 частей: incident_id, service, severity, duration_raw, channel, acknowledged_raw
    if len(parts) != 6:
        raise IncidentFormatError(f"Неверный формат строки: ожидается 6 частей, получено {len(parts)}: {row}")
    incident_id, service, severity, duration_raw, channel, acknowledged_raw = parts
    # TODO: duration_raw преобразовать в float
    try:
        duration = float(duration_raw)
    except ValueError as exc:
        raise DurationError(f"Некорректный формат длительности: '{duration_raw}'") from exc
    # TODO: проверить, что duration > 0
    if duration <= 0:
        raise DurationError(f"Длительность должна быть положительной, получено {duration} мин")
    # TODO: проверить severity в {'low', 'medium', 'high', 'critical'}
    valid_severities = {'low', 'medium', 'high', 'critical'}
    if severity not in valid_severities:
        raise SeverityError(f"Неизвестный уровень приоритета: '{severity}'. Допустимые значения: {valid_severities}")
    # TODO: проверить channel в {'email', 'slack', 'pager'}
    valid_channels = {'email', 'slack', 'pager'}
    if channel not in valid_channels:
        raise ChannelError(f"Неизвестный канал связи: '{channel}'. Допустимые каналы: {valid_channels}")
    # TODO: проверить acknowledged_raw в {'yes', 'no'}
    if acknowledged_raw not in {'yes', 'no'}:
        raise AcknowledgedFlagError(f"Некорректный флаг подтверждения: '{acknowledged_raw}'. Допустимые значения: 'yes', 'no'")
    # TODO: превратить acknowledged_raw в bool
    acknowledged = acknowledged_raw == 'yes'
    # TODO: вернуть словарь с разобранными полями
    return {
        'incident_id': incident_id,
        'service': service,
        'severity': severity,
        'duration_min': duration,
        'channel': channel,
        'acknowledged': acknowledged
    }

def process_batch(rows):
    # TODO: создать списки incidents и errors
    incidents = []
    errors = []
    # TODO: пройтись по rows циклом
    for row in rows:
        # TODO: внутри try вызвать parse_incident(row)
        try:
            incident = parse_incident(row)
            # TODO: валидный incident добавить в incidents
            incidents.append(incident)
        except IncidentProcessingError as e:
            # TODO: IncidentProcessingError сохранить в errors как (row, error_type, message)
            error_type = type(e).__name__
            errors.append((row, error_type, str(e)))
    # TODO: вернуть (incidents, errors)
    return incidents, errors

# TODO: вызвать process_batch(rows)
incidents, errors = process_batch(rows)


# TODO: вывести количество валидных инцидентов и количество ошибок
print(f"Количество валидных инцидентов: {len(incidents)}")
print(f"Количество ошибок: {len(errors)}")

# TODO: собрать error_counts: dict[str, int]
error_counts = {}
for _, error_type, _ in errors:
    error_counts[error_type] = error_counts.get(error_type, 0) + 1

# TODO: собрать unacked_by_channel: dict[str, list[str]] только для acknowledged == False
unacked_by_channel = {}
for incident in incidents:
    if not incident['acknowledged']:
        channel = incident['channel']
        if channel not in unacked_by_channel:
            unacked_by_channel[channel] = []
        unacked_by_channel[channel].append(incident['incident_id'])

# TODO: собрать average_duration_by_severity только по валидным строкам
average_duration_by_severity = {}
severity_durations = {}
for incident in incidents:
    severity = incident['severity']
    duration = incident['duration_min']
    if severity not in severity_durations:
        severity_durations[severity] = []
    severity_durations[severity].append(duration)

for severity, durations in severity_durations.items():
    average_duration_by_severity[severity] = sum(durations) / len(durations)

# TODO: найти longest_incident среди валидных инцидентов по duration_min
longest_incident = None
max_duration = -1
for incident in incidents:
    if incident['duration_min'] > max_duration:
        max_duration = incident['duration_min']
        longest_incident = incident

# TODO: красиво вывести получившиеся структуры
print("\n--- Статистика по ошибкам ---")
for error_type, count in error_counts.items():
    print(f"{error_type}: {count}")


print("\n--- Неподтверждённые инциденты по каналам ---")
for channel, incident_ids in unacked_by_channel.items():
    print(f"Канал '{channel}': {incident_ids}")

print("\n--- Средняя длительность по уровням приоритета ---")
for severity, avg_duration in average_duration_by_severity.items():
    print(f"Приоритет '{severity}': {avg_duration:.2f} мин")

print("\n--- Самый длительный инцидент ---")
if longest_incident:
    print(f"ID: {longest_incident['incident_id']}, "
          f"сервис: {longest_incident['service']}, "
          f"длительность: {longest_incident['duration_min']} мин, "
          f"приоритет: {longest_incident['severity']}")
else:
    print("Нет валидных инцидентов")
