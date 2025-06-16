from rich.console import Console
from itertools import permutations

console = Console()
main_color = '#8A2BE2'
data = ['james', '07082008', 'marry', 'alex', 'sam']
chars = ''.join(sorted('qwertyuiopasdfghjklzxcvbnm'))

def combined_passwords(data):
    chars = ''.join(sorted('qwertyuiopasdfghjklzxcvbnm'))
    console.print("Перебор по данным: \n", style=f'bold italic {main_color}')

# -----------------------

    for datas in data:
        console.print(f"->   {datas}\n", style=f'bold {main_color}')
    
    combines = []
    for its in range(1, len(data) + 1):
        for attempt in permutations(data, its):
            combines.append(''.join(attempt).upper())
            combines.append(''.join(attempt).lower())
    console.print(f"Всего найдено: {len(combines)} базовых паролей", style=f'bold {main_color}')

# -----------------------

    first_upper_data = []
    for name in data:
        if name[0] in chars:
            first_upper_data.append(name[0].upper() + name[1:])
        else:
            first_upper_data.append(name)
    combines_upper = []
    for its in range(1, len(data) + 1):
        for attempt in permutations(first_upper_data, its):
            combines_upper.append(''.join(attempt))
    console.print(f"Всего найдено: {len(combines_upper)} комбинаций паролей с первой заглавной", style=f'bold {main_color}')

# -----------------------

    first_lower_data = []
    for name in data:
        if name[0] in chars:
            first_lower_data.append(name[0].lower() + name[1:])
        else:
            first_lower_data.append(name)
    combines_lower = []
    for its in range(1, len(data) + 1):
        for attempt in permutations(first_lower_data, its):
            combines_lower.append(''.join(attempt))
    console.print(f"Всего найдено: {len(combines_lower)} комбинаций паролей с первой строчной", style=f'bold {main_color}')
    
# -----------------------

    combines_upper_only = []
    for its in range(1, len(data) + 1):
        for attempt in permutations(data, its):
            names = ''.join(attempt)
            combines_upper_only.append(names[0].upper() + names[1:])
    console.print(f"Всего найдено: {len(combines_upper_only)} комбинаций паролей только с первой заглавной", style=f'bold {main_color}')

# -----------------------
    first_lower_only = []
    for name in data:
        if name[0] in chars:
            first_lower_only.append(name[0].upper() + name[1:])
        else:
            first_lower_only.append(name)
    combines_lower_only = []
    for its in range(1, len(data) + 1):
        for attempt in permutations(first_lower_only, its):
            names = ''.join(attempt)
            combines_lower_only.append(names[0].lower() + names[1:])
    console.print(f"Всего найдено: {len(combines_upper_only)} комбинаций паролей только с первой строчной", style=f'bold {main_color}')

    concl = set()
    for name in combines:
        concl.add(name)
    for name in combines_upper:
        concl.add(name)
    for name in combines_lower:
        concl.add(name)
    for name in combines_upper_only:
        concl.add(name)
    for name in combines_lower_only:
        concl.add(name)
    
    console.print(f"Всего найдено: {len(concl)} уникальных паролей", style=f'bold {main_color}')

combined_passwords(data)