subscriptions = {
    "Alice": {"music", "video"},
    "Bob": {"music"},
    "Dina": set(),
}

commands = [
    "add|Dina|books",
    "remove|Alice|video",
    "remove|Bob|cloud",
    "report",
    "undo",
    "add|Bob|cloud",
    "undo",
    "undo",
    "report",
]

history_stack = []
reports = []
errors = []
undo_count = 0

for command in commands:
    if command == "undo":
        # TODO 1: проверьте, что history_stack не пуст
        if history_stack:
            subscriptions = history_stack.pop()
            # TODO 3: присвойте subscriptions извлечённое состояние
            # TODO 4: увеличьте undo_count на 1
            undo_count +=1
            # TODO 5: если стек пуст, просто пропустите команду
        continue

    if command == "report":
        # TODO 6: сделайте независимую копию subscriptions
        current_report = {}
        for user, services in subscriptions.items():
            current_report[user] = services.copy()  # копируем set отдельно
        # TODO 7: добавьте копию в reports
        reports.append(current_report)
        continue

    action, user, service = command.split("|")
    current_services = subscriptions.get(user, set())

    if action == "add":
        # TODO 8: перед изменением сохраните снимок subscriptions в history_stack
        snapshot = {}
        for u, s in subscriptions.items():
            snapshot[u] = s.copy()
        history_stack.append(snapshot)
        # TODO 9: если user отсутствует, создайте для него пустой set
        if user not in subscriptions:
            subscriptions[user] = set()
        # TODO 10: добавьте service в subscriptions[user]
        subscriptions[user].add(service)

    elif action == "remove":
        # TODO 11: если service отсутствует у пользователя,
        if service not in current_services:
            errors.append(f"Ошибка: сервис '{service}' не найден у пользователя '{user}'")
        else:
            # TODO 12: если service есть,
            # сначала сохраните снимок subscriptions в history_stack,
            snapshot = {}
            for u, s in subscriptions.items():
                snapshot[u] = s.copy()
            history_stack.append(snapshot)
            # затем удалите service из subscriptions[user]
            subscriptions[user].remove(service)

print("Отчёты:", reports)
print("Ошибки:", errors)
print("Успешных undo:", undo_count)
print("Финальные подписки:", subscriptions)