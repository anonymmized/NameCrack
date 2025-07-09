import argparse
from rich.console import Console
from itertools import permutations
from check_pas import pwned_api_check
from find_dates import dates_processing
from find_mails_logins import mails_processing, logins_processing 
from find_names import names_processing
from find_number import numbers_processing
from do_leet_speak_reversed import leet_speak_word, reverse_word
from find_colors_nums import colors_processing, num_processing
# TODO: Сохранение паролей в разных форматах

# TODO: Полная реконструкция структуры функции для добавления аргументов

console = Console()
main_color = '#8A2BE2'
text = '98234 Alexs'

def combined_passwords(text):
    words = text.split()
    mails = mails_processing(text)
    names = names_processing(text)
    numbers = numbers_processing(text)
    colors = colors_processing(text)
    nums = num_processing(text)
    logins = set()
    for word in words:
        logins.update(logins_processing(word))
    dates = dates_processing(text)
    console.print("Перебор по данным:", style=f'bold italic {main_color}')
    combines = []
    for word in words:
        console.print(f"->   {word}", style=f'bold {main_color}')
    if mails:
        console.print(f"Mails: {mails}", style=f'bold {main_color}')
        combines += [mail for mail in mails]
    if logins:
        console.print(f"Logins: {logins}", style=f'bold {main_color}')
        combines += [login for login in logins]
    if dates:
        console.print(f"Dates: {dates}", style=f'bold {main_color}')
        combines += [date for date in dates]
    if names:
        console.print(f"Names: {names}", style=f'bold {main_color}')
        combines += [name for name in names]
    if numbers:
        console.print(f"Numbers: {numbers}", style=f'bold {main_color}')
        combines += [number for number in numbers]
    if colors:
        console.print(f"Colors: {colors}", style=f'bold {main_color}')
        combines += [color for color in colors]
    if nums:
        console.print(f"Nums: {nums}", style=f'bold {main_color}')
        combines += [num for num in nums]

    for r in range(1, min(4, len(words) + 1)):
        for attempt in permutations(words, r):
            combined = ''.join(attempt)
            if len(combined) >= 6:
                # combines.append(leet_speak_word(combined))
                # combines.append(reverse_word(combined))
                # combines.append(combined.upper())
                combines.append(combined.lower())
    unique_passwords = set(combines)
    console.print(f"Всего уникальных паролей: {len(unique_passwords)}", style=f'bold {main_color}')
    for pas in unique_passwords:
        try:
            cnt = pwned_api_check(pas)
            console.print(f"Password: {pas} - {cnt}", style=f'bold {main_color}', markup=False)
        except Exception as e:
            console.print(f"Error checking password {pas}: {e}", style='bold red', markup=False)


def main():
    parser = argparse.ArgumentParser(description="Генератор паролей на основе текста")

    parser.add_argument('-t', '--text', help='Входной текст для анализа', required=True)
    parser.add_argument('-lt', '--leet', action='store_true', help='Добавить Leet Speak варианты')
    parser.add_argument('-rv', '--reverse', action='store_true', help='Добавить перевернутые варианты')
    parser.add_argument('-up', '--upper', action='store_true', help='Добавить варианты с верхним регистром')
    parser.add_argument('--min-length', type=int, default=6, help='Определить минимальную длину пароля')
    parser.add_argument('--max-length', type=int, default=12, help='Определить максимальную длину пароля')

    args = parser.parse_args()


combined_passwords(text)