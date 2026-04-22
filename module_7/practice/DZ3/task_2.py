# Дантекстовыйфайл.Необходимосоздатьновыйфайл 
# и записать в него следующую статистику по исходному 
# файлу:
# ■ Количество символов;
# ■ Количество строк;
# ■ Количество гласных букв;
# ■ Количество согласных букв;
# ■ Количество цифр

def analyze_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    total_chars = 0
    lines = 0
    vowels = 0  
    consonants = 0   
    digits = 0       
    
    for char in content:
        total_chars += 1
        
        if char.isdigit():
            digits += 1
        
        if char.lower() in 'аеёиоуыэюя':
            vowels += 1

        elif char.isalpha():
            consonants += 1
            
        if char == '\n':
            lines += 1
    

    with open(output_file, 'w', encoding='utf-8') as out_file:
        out_file.write(f"Количество символов: {total_chars}\n")
        out_file.write(f"Количество строк: {lines}\n")
        out_file.write(f"Гласных букв: {vowels}\n")
        out_file.write(f"Согласных букв: {consonants}\n")
        out_file.write(f"Цифр: {digits}\n")

input_file = 'input.txt'  
output_file = 'output.txt' 
analyze_file(input_file, output_file)
