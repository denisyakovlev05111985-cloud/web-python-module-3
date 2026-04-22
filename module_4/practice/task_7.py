def simbol_v_texte(text):
    text = text.replace(" ","")  # убираем пробелы
    max_count= 0
    char_res= ''

    for char in text:
        count= text.count(char)
        if count > max_count:
            max_count = count
            char_res = char
    return char_res



print(simbol_v_texte('Hello oo wer   '))