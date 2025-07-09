from colour import Color
# Поиск названий цветов в тексте
def colors_processing(text):
    colors = []
    for word in text.split():
        try:
            if Color(word): # Используется функция для поиска названий цветов
                colors.append(word.lower())
        except ValueError: # Обработка ошибок
            continue
    return colors
# Поиск цифр в тексте
def num_processing(text):
    nums = []
    for num in text.split(): 
        if num.isdigit(): # Если строку можно представить в виде символов строка добавляется в массив
            nums.append(num)
    return nums