# проверить на палиндром
stroka= input('')

stroka = stroka.lower().replace(" ", "") # переводим строку к единому регистру и убираем пробелы

if stroka == stroka[::-1]:
    print('палиндром')
else:
    print('не палиндром')