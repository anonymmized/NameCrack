import re 
from datetime import datetime

def dates_processing(text):
    current_year = datetime.now().year % 100
    MONTHS = {
        'jan': ['january', 'jan', 'янв', '01'],
        'feb': ['february', 'feb', 'фев', '02'],
        'mar': ['march', 'mar', 'мар', '03'],
        'apr': ['april', 'apr', 'апр', '04'],
        'may': ['may', 'май', '05'],
        'jun': ['june', 'jun', 'июн', '06'],
        'jul': ['july', 'jul', 'июл', '07'],
        'aug': ['august', 'aug', 'авг', '08'],
        'sep': ['september', 'sep', 'сен', '09'],
        'oct': ['october', 'oct', 'окт', '10'],
        'nov': ['november', 'nov', 'ноя', '11'],
        'dec': ['december', 'dec', 'дек', '12']
    }

    DATE_REGEXES = [
        r'\b(\d{1,2})\s+([a-zA-Zа-яА-Я]+)\s+(\d{4})\b',  
        r'\b([a-zA-Zа-яА-Я]+)\s+(\d{1,2})\s+(\d{4})\b',  
        r'\b(\d{4})\s+([a-zA-Zа-яА-Я]+)\s+(\d{1,2})\b',  
        r'\b(\d{1,2})[\/\.\-](\d{1,2})[\/\.\-](\d{2,4})\b',  
        r'\b(\d{4})-(\d{1,2})-(\d{1,2})\b',  
        r'\b(\d{2})([a-zA-Zа-яА-Я]{3})(\d{2,4})\b'
    ]
    found_dates = set()

    for regex in DATE_REGEXES:
        matches = re.findall(regex, text, re.IGNORECASE)
        for match in matches:
            if len(match) == 3:
                part1, part2, part3 = match

                if regex == DATE_REGEXES[-1]:
                    day, month, year = part1, part2, part3
                    if month.lower() in sum(MONTHS.values(), []):
                        month_abbr = next(key for key, value in MONTHS.items() if month.lower() in value)
                        if len(year) == 2:
                            year = "20" + year if int(year) <= current_year else "19" + year
                        found_dates.add(f"{day.zfill(2)}{month_abbr.upper()}{year}")
                        found_dates.add(f"{year}{month_abbr.upper()}{day.zfill(2)}")

                elif any(part2.lower() in month_list for month_list in MONTHS.values()):
                    month_abbr = next(key for key, value in MONTHS.items() if part2.lower() in value)
                    day = part1.zfill(2) if part1.isdigit() else part3.zfill(2)
                    year = part3 if part3.isdigit() and len(part3) == 4 else part1
                    found_dates.add(f"{day}{month_abbr.upper()}{year}")
                    found_dates.add(f"{year}{month_abbr.upper()}{day}")
                
                elif part1.isdigit() and part2.isdigit() and part3.isdigit():
                    d, m, y = part1, part2, part3
                    if len(y) == 2:
                        y = "20" + y if int(y) <= current_year else "19" + y
                    found_dates.add(f"{d.zfill(2)}{m.zfill(2)}{y}")
                    found_dates.add(f"{y}{m.zfill(2)}{d.zfill(2)}")

    return list(found_dates)