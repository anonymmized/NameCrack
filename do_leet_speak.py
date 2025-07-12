import random 

# Словарь с символами Leet Speak
LEET_MAP = {
    'a': ['4', '@', '^'],
    'b': ['8', '|3', 'I3', '!3'],
    'd': ['|)', '!)'],
    'e': ['3'],
    'f': ['|=', 'ƒ', 'ph'],
    'g': ['6', '9'],
    'i': ['1', '!', '|', '!'],
    'k': ['|<', '|{', '|(', '|C'],
    'l': ['1', '!', '|'],
    'm': ['//', '^^', 'IVI'],
    'o': ['0', '()', '[]'],
    'p': ['|^', '|*', '|°', '|D', 'р'],
    's': ['5', '$', '§', 'z', "$"],
    't': ['7', 'т'],
    'x': ['><', '}{'],
    '0': ['o', 'О'],
    '1': ['i', 'l'],
    '2': ['z'],
    '3': ['e'],
    '4': ['a'],
    '5': ['s'],
    '6': ['g', 'б'],
    '8': ['b', 'В'],
    '9': ['g']
}

def leet_speak_word(word, flag=None):
    updated_word = []
    
    for ind, char in enumerate(word.lower()): # Перебор каждого символа по индексу и символу
        replaced = False # Флаг №1
        should_replace = True # Флаг №2
        if flag is True and ind % 2 != 0: # Проверки по флагам
            should_replace = False
        elif flag is False and ind % 2 == 0:
            should_replace = False
        if should_replace:
            for key, values in LEET_MAP.items(): # Перебор словаря и составление пароля уже Leet Speak
                if char == key:
                    updated_word.append(random.choice(values))
                    replaced = True
                    break
        if not replaced:
            updated_word.append(char) # Добавление пароля в список

    return ''.join(updated_word)

