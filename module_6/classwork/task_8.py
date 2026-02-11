logs= {
    ('ivan','d1','login'),
    ('ivan','d1','view'),
    ('ivan','d2','login'),
    ('olga','d1','login'),
    ('petr','d2','error'),
    ('anna','d1','login'),
    ('anna','d2','view'),
}

action_count= {}
days= {}
actions= {}

for name, day, action in logs:
    action_count[name] = action_count.get(name, 0) + 1

    if name not in actions:
        actions[name] = set()
    actions[name].add(action)

user_error= []
for name, action in actions.items():
    if 'error' in action and 'login' not in action:
        user_error.append(name)

print(action_count)
print(actions)
print(user_error)