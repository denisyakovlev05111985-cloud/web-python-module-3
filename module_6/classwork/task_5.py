# Найти друзей его друзей. которых нет в его друзьях

network= {
    "Me": {"Alise", "Bob"},
    "Alise": {"Me", "Chalie", "Bob"},
    "Bob": {"Me", "David", "Eve"},
    "Charlie": {"Alise"},
    "David": {"Alise", "Bob"},
    "Eve": {"Bob"}
}

frend_me= network["Me"]
frends_obchie= set()

for el in frend_me:
    frends_obchie.update(network[el])

frends_obchie.discard("Me")

difference_frend= frends_obchie - frend_me

print(difference_frend)
    


# Ответ : Charlie, David, Eve