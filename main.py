from rich.console import Console
from itertools import permutations
from check_pas import pwned_api_check
from find_dates import dates_processing

console = Console()
main_color = '#8A2BE2'
text = '07jan2008 08jun09'

def combined_passwords(text):
    words = text.split()
    dates = dates_processing(text)
    print(dates)
    console.print("Перебор по данным:", style=f'bold italic {main_color}')
    for word in words:
        console.print(f"->   {word}", style=f'bold {main_color}')
    
    combines = []
    combines += [date for date in dates]
    for r in range(1, len(words) + 1):
        for attempt in permutations(words, r):
            combined = ''.join(attempt)
            combines.append(combined.upper())
            combines.append(combined.lower())
    
    console.print(f"Всего найдено: {len(combines)} базовых паролей", style=f'bold {main_color}')
    unique_passwords = set(combines)
    console.print(f"Всего найдено: {len(unique_passwords)} уникальных паролей", style=f'bold {main_color}')
    for pas in unique_passwords:
        try:
            cnt = pwned_api_check(pas)
            console.print(f"Password: {pas} - {cnt}", style=f'bold {main_color}')
        except Exception as e:
            console.print(f"Error checking password {pas}: {e}", style='bold red')

combined_passwords(text)