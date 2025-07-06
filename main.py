from rich.console import Console
from itertools import permutations
from check_pas import pwned_api_check
from find_dates import dates_processing
from find_mails_logins import mails_processing, logins_processing 
from find_names import names_processing
from find_number import numbers_processing
from do_leet_speak_reversed import leet_speak_word, reverse_word
# TODO: Добавить аргументы для обработки функций leet_speak_word и reverse_word

console = Console()
main_color = '#8A2BE2'
text = '070882'

def combined_passwords(text):
    words = text.split()
    mails = mails_processing(text)
    names = names_processing(text)
    numbers = numbers_processing(text)
    logins = set()
    for word in words:
        logins.update(logins_processing(word))
    dates = dates_processing(text)
    console.print("Перебор по данным:", style=f'bold italic {main_color}')
    for word in words:
        console.print(f"->   {word}", style=f'bold {main_color}')
    if mails:
        console.print(f"Mails: {mails}", style=f'bold {main_color}')
    if logins:
        console.print(f"Logins: {logins}", style=f'bold {main_color}')
    if dates:
        console.print(f"Dates: {dates}", style=f'bold {main_color}')
    if names:
        console.print(f"Names: {names}", style=f'bold {main_color}')
    if numbers:
        console.print(f"Numbers: {numbers}", style=f'bold {main_color}')
    combines = []
    combines += [date for date in dates]
    combines += [mail for mail in mails]
    combines += [login for login in logins]
    for r in range(1, min(4, len(words) + 1)):
        for attempt in permutations(words, r):
            combined = ''.join(attempt)
            if len(combined) >= 6:
                # combines.append(leet_speak_word(combined))
                # combines.append(reverse_word(combined))
                combines.append(combined.upper())
                combines.append(combined.lower())
    unique_passwords = set(combines)
    console.print(f"Всего уникальных паролей: {len(unique_passwords)}", style=f'bold {main_color}')
    for pas in unique_passwords:
        try:
            cnt = pwned_api_check(pas)
            console.print(f"Password: {pas} - {cnt}", style=f'bold {main_color}', markup=False)
        except Exception as e:
            console.print(f"Error checking password {pas}: {e}", style='bold red', markup=False)

combined_passwords(text)