
# Дано два текстовых файла. Выяснить, совпадают ли 
# их строки. Если нет, то вывести несовпадающую строку 
# из каждого файла.

def compare_files(file1, file2):
    try:
        with open(file1, 'r', encoding='utf-8') as f1, \
             open(file2, 'r', encoding='utf-8') as f2:
            
            lines1 = f1.readlines()
            lines2 = f2.readlines()

            if len(lines1) != len(lines2):
                print("Файлы имеют разную длину")
                return

            for i in range(len(lines1)):
                if lines1[i].strip() != lines2[i].strip():
                    print(f"Несовпадающие строки:")
                    print(f"Файл 1: {lines1[i].strip()}")
                    print(f"Файл 2: {lines2[i].strip()}")
                    return

        print("Все строки совпадают")

    except FileNotFoundError:
        print(f"Ошибка: файл {file1} или {file2} не найден")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

compare_files('file1.txt', 'file2.txt')