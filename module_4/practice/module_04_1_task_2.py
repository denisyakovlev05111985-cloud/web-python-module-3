# Пользователь вводит с клавиатуры некоторый текст, 
# после из зарезервированных 
# слов необходимо найти и изменить их регистр на верхний. Вывести на 
# экран измененный текст. 

text= input('') # текст для проверки - Да здравствует мир труд май 
rezerv_slov= 'мир труд май'

razbiv_text= text.split()
razbiv_rezerv= rezerv_slov.split()

for el in range(len(razbiv_text)):
    for el_2 in range(len(razbiv_rezerv)):
        if razbiv_text[el] == razbiv_rezerv[el_2]:
            razbiv_text[el] = razbiv_text[el].upper()
result = ' '.join(razbiv_text)

print("Измененный текст:")
print(result) # Да здравствует МИР ТРУД МАЙ
