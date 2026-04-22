# file= open('file.txt', 'r')

# print(file.read(1))
# print(file.read(1))

# file.close()

# r - чтение
# w - запись с очисткой
# a - дозапись текста в конец файла
# x - создает новый файл
# t - текстовый режим
# b - бинарный режим ... картинки видео
# + - чтение и запись

# передаем через обычный слеш /, либо экранируем через два обратных \\

# file= open('file.txt', 'w')
# file.write('54321')
# file.close()


# file= open('file.txt', 'a', encoding='utf-8')
# file.write('-добавили в конец')
# file.close()

# f= open('file.txt', 'a', encoding='utf-8')
# f.write('1,2,3\n')
# f.write('4,5,6\n')
# f.write('7,8,9\n')
# f.close()

# f= open('file.txt', 'r', encoding='utf-8')
# print(f.readline().strip())
# print(f.readline().strip())
# for line in f:
#     print(line.strip())

with open('file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip()) 