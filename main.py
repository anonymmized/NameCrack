import time
import argparse
from rich.console import Console
from itertools import permutations
from project_ascii import print_art
from check_pas import pwned_api_check
from find_names import names_processing
from find_dates import dates_processing
from find_number import numbers_processing
from find_colors_nums import colors_processing, num_processing
from do_leet_speak import leet_speak_word
from find_mails_logins import mails_processing, logins_processing
from export_data import export_data

console = Console()
MAIN_COLOR = '#8A2BE2'

def password_processing(text, leet=False, flag=None, reverse=False, uppr=False, min_length=6, max_length=12):
    """Processes the input text to generate potential passwords based on various transformations and checks.
    
    Args:
        text (str): Input text to analyze
        leet (bool): Whether to apply leet speak transformations
        flag (bool|None): Flag for selective leet conversion
        reverse (bool): Whether to add reversed versions of strings
        uppr (bool): Whether to add uppercase versions of strings
        min_length (int): Minimum length for passwords
        max_length (int): Maximum length for passwords
        
    Returns:
        set: Unique generated passwords
    """
    if not text or not isinstance(text, str):
        console.print("❌ Invalid text input. Please provide non-empty text.", style='bold red')
        return set()
    
    words = text.split()
    names = names_processing(text)
    dates = dates_processing(text)
    numbers = numbers_processing(text)
    nums = num_processing(text)
    colors = colors_processing(text)
    mails = mails_processing(text)
    logins = set()
    for word in words:
        logins.update(logins_processing(word))
    console.print('Iterating through data to generate passwords:', style=f'bold italic {MAIN_COLOR}')
    combines = []
    for word in words:
        console.print(f"-> {word}", style=f"bold {MAIN_COLOR}")
    if names:
        console.print(f"Names: {names}", style=f"bold {MAIN_COLOR}")
        combines += [name for name in names]
    if dates:
        console.print(f"Dates: {dates}", style=f"bold {MAIN_COLOR}")
        combines += [date for date in dates]
    if numbers:
        console.print(f"Numbers: {numbers}", style=f"bold {MAIN_COLOR}")
        combines += [number for number in numbers]
    if nums:
        console.print(f"Nums: {nums}", style=f"bold {MAIN_COLOR}")
        combines += [num for num in nums]
    if colors:
        console.print(f"Colors: {colors}", style=f"bold {MAIN_COLOR}")
        combines += [color for color in colors]
    if mails:
        console.print(f"Mails: {mails}", style=f"bold {MAIN_COLOR}")
        combines += [mail for mail in mails]
    if logins:
        console.print(f"Logins: {logins}", style=f"bold {MAIN_COLOR}")
        combines += [login for login in logins]
    for r in range(1, min(4, len(words) + 1)):
        for attempt in permutations(words, r):
            combined = ''.join(attempt)
            if min_length <= len(combined) <= max_length:
                combines.append(combined.lower())
                if uppr == True:
                    combines.append(combined.upper())
                if leet == True and flag == None:
                    combines.append(leet_speak_word(combined))
                elif leet == True and flag == True:
                    combines.append(leet_speak_word(combined, True))
                elif leet == True and flag == False:
                    combines.append(leet_speak_word(combined, False))
                if reverse:
                    combines.append(combined[::-1])
    unique_passwords = set(combines)
    console.print(f"Unique passwords: {len(unique_passwords)}", style=f"bold {MAIN_COLOR}")
    return unique_passwords


def main():
    art = print_art()
    console.print(art, style='bold purple')
    time.sleep(2.5)
    parser = argparse.ArgumentParser(description="Password generator based on text")

    parser.add_argument('-t', '--text', type=str, required=True, help='Input text for analysis. Must be a non-empty string.')
    parser.add_argument('-lt', '--leet', action='store_true', help='Add leet speak options')
    parser.add_argument('-rv', '--reverse', action='store_true', help='Add reversed options')
    parser.add_argument('-up', '--upper', action='store_true', help='Add options with the upper registry')
    parser.add_argument('--min-length', type=int, default=6, help='Determine the minimum password length (must be a positive integer)')
    parser.add_argument('--max-length', type=int, default=12, help='Determine the maximum password length (must be equal or greater than minimum length)')
    parser.add_argument('--json', action='store_true', help='Export passwords in JSON format')
    parser.add_argument('--xml', action='store_true', help='Export passwords in XML format')

    args = parser.parse_args()
    
    # Validate length arguments
    if args.min_length <= 0:
        console.print("❌ Minimum password length must be a positive integer.", style='bold red')
        return
    if args.max_length < args.min_length:
        console.print("❌ Maximum password length cannot be less than minimum password length.", style='bold red')
        return

    if args.leet:
        console.print("Additional option for leet speak", style=f"{MAIN_COLOR}")
        console.print("For even characters - True", style=f"{MAIN_COLOR}")
        console.print("For odd characters - False", style=f"{MAIN_COLOR}")
        flag_value = console.input("Enter T/F: ")
        if flag_value == "T".lower():
            passwords = password_processing(args.text, args.leet, True, args.reverse, args.upper, args.min_length, args.max_length)
        elif flag_value == "F".lower():
            passwords = password_processing(args.text, args.leet, False, args.reverse, args.upper, args.min_length, args.max_length)
        else:
            passwords = password_processing(args.text, args.leet, None, args.reverse, args.upper, args.min_length, args.max_length)
    else:
        passwords = password_processing(args.text, args.leet, True, args.reverse, args.upper, args.min_length, args.max_length)
    # Check passwords against HaveIBeenPwned database
    console.print("\n🔍 Checking passwords against breach databases...", style=f"bold {MAIN_COLOR}")
    counted_passwords = {}
    for pas in passwords:
        try: 
            breach_count = pwned_api_check(pas)
            if breach_count > 0:
                counted_passwords[pas] = breach_count
        except Exception as e:
            console.print(f"Error checking password {pas}: {e}", style='bold red', markup=False)
    
    # Display results
    console.print(f"\n📊 Results:", style=f"bold {MAIN_COLOR}")
    console.print(f"Total passwords generated: {len(passwords)}", style=f"bold {MAIN_COLOR}")
    console.print(f"Compromised passwords found: {len(counted_passwords)}", style=f"bold {MAIN_COLOR}")
    
    if counted_passwords:
        console.print(f"\n⚠️  Compromised passwords:", style='bold red')
        for password, count in counted_passwords.items():
            console.print(f"  - {password}: {count} breaches", style='bold red')
    
    # Handle exports
    if args.json:
        export_data(passwords, counted_passwords, 'json')
    
    if args.xml:
        export_data(passwords, counted_passwords, 'xml')
    
    return passwords, counted_passwords

if __name__ == "__main__":
    passwords, compromised_passwords = main()
    if not compromised_passwords:
        console.print("\n✅ No compromised passwords found!", style='bold green')
