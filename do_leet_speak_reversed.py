import random 

LEET_MAP = {
    'a': ['4', '@', '/\\', '/-\\', '^', '(L)'],
    'b': ['8', '|3', 'I3', '!3', ')3', 'ß', 'в'],
    'c': ['[', '{', '(', '¢', '©'],
    'd': ['|)', '!)', '|>', '1)'],
    'e': ['3', '€', 'ë', '[-'],
    'f': ['|=', 'ƒ', 'ph'],
    'g': ['6', '9', '&', '(_+', 'C-'],
    'h': ['#', '|-|', '][-]', ':', ']-['],
    'i': ['1', '!', '|', '][', '!'],
    'j': ['_', '_]', ';'],
    'k': ['|<', '|{', '|(', '|C'],
    'l': ['1', '!', '7', '|_', '|'],
    'm': ['|\\/|', '|V|', '//', '^^', 'IVI'],
    'n': ['|\\|', '/\\/', 'И', '][', '/\\|'],
    'o': ['0', '()', '[]', '{}', 'oh'],
    'p': ['|^', '|*', '|°', '|D', 'р'],
    'q': ['0,', '()-', '(|)', '9', '(&'],
    'r': ['2', 'Я', '|2', '|?', '|S', '|Z'],
    's': ['5', '$', '§', 'z', "'$"],
    't': ['7', '+', "-|-", '"|"', 'т'],
    'u': ['|_|', '(_)', 'µ', 'ц'],
    'v': ['\\/', '|/', '\\/'],
    'w': ['\\/\\/', '\\X/', 'VV', 'Ш', 'Щ', 'Э'],
    'x': ['><', '}{', '%', 'Ж', 'Х'],
    'y': ['\\"/', '¥', 'Ч', 'У'],
    'z': ['2', '($)'],
    '0': ['o', 'О'],
    '1': ['i', 'l', 'Й', 'И'],
    '2': ['z', 'З', 'з'],
    '3': ['e', 'Е', 'е'],
    '4': ['a', 'А', 'а'],
    '5': ['s', 'С', 'с'],
    '6': ['g', 'б'],
    '7': ['t', 'Т', 'т'],
    '8': ['b', 'В', 'в'],
    '9': ['g', 'г']
}

def leet_speak_word(word, flag=None):
    updated_word = []
    
    for ind, char in enumerate(word.lower()):
        replaced = False
        should_replace = True
        if flag is True and ind % 2 != 0:
            should_replace = False
        elif flag is False and ind % 2 == 0:
            should_replace = False
        if should_replace:
            for key, values in LEET_MAP.items():
                if char == key:
                    updated_word.append(random.choice(values))
                    replaced = True
                    break
        if not replaced:
            updated_word.append(char)

    return ''.join(updated_word)

def reverse_word(word):
    return word[::-1]

word = 'alex'
leet_word = leet_speak_word(word)
reversed_word = reverse_word(word)
print(leet_word, reversed_word)