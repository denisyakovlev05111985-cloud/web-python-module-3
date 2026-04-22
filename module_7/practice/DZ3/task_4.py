# Дан текстовый файл. Найти длину самой длинной 
# строки.

def find_max_line_length(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
        max_length = 0
        
        for line in lines:

            line_length = len(line.strip())
            
            if line_length > max_length:
                max_length = line_length
                
    return max_length

file_path = 'file1.txt'
max_len = find_max_line_length(file_path)
print(f"Длина самой длинной строки: {max_len} символов")