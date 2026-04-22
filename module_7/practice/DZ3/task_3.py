# Дан текстовый файл. Удалить из него последнюю 
# строку. Результат записать в другой файл.

def remove_last_line(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        if not lines:
            print("Файл пуст")
            return
        
        lines = lines[:-1]
        
        with open(output_file, 'w', encoding='utf-8') as new_file:
            new_file.writelines(lines)
            
        print(f"Операция выполнена. Результат сохранен в {output_file}")
        
    except FileNotFoundError:
        print("Исходный файл не найден")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

input_filename = 'file1.txt' 
output_filename = 'file3.txt'
remove_last_line(input_filename, output_filename)