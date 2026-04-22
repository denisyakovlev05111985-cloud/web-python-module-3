history= [
    ('t_1', 'new'),('t_1', 'in_progress'),('t_1', 'done'),
    ('t_2', 'new'), ('t_2', 'done'),
    ('t_3', 'new'),('t_3', 'in_progress'),('t_3', 'cancelled'),
    ('t_4', 'new'),('t_4', 'cancelled'),('t_4', 'done')
]

kortegi= {
    ('new', 'in_progress'),
    ('in_progress', 'done'),
    ('new', 'cancelled'),
    ('in_progress', 'cancelled'),
}

last_status= {}
errors= {}

for el, status in history:
    if el not in last_status:
        last_status[el]= status
        continue
        
    prev= last_status[el]
    if (prev, status) not in kortegi:
        if el not in errors:
            errors[el] = (prev, status)
    else:
        last_status[el]= status

for el, transition in errors.items():
    print(el, ":", transition)
