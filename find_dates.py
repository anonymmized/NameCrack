import re
from datetime import datetime

def dates_processing(text):
    MONTHS = {
        'jan': ['january', 'jan', 'янв', '01', '1'],
        'feb': ['february', 'feb', 'фев', '02', '2'],
        'mar': ['march', 'mar', 'мар', '03', '3'],
        'apr': ['april', 'apr', 'апр', '04', '4'],
        'may': ['may', 'май', '05', '5'],
        'jun': ['june', 'jun', 'июн', '06', '6'],
        'jul': ['july', 'jul', 'июл', '07', '7'],
        'aug': ['august', 'aug', 'авг', '08', '8'],
        'sep': ['september', 'sep', 'сен', '09', '9'],
        'oct': ['october', 'oct', 'окт', '10'],
        'nov': ['november', 'nov', 'ноя', '11'],
        'dec': ['december', 'dec', 'дек', '12']
    }

    found_dates = set()

    current_year_short = datetime.now().year % 100
    six_digit_matches = re.findall(r'\b\d{6}\b', text)
    for match in six_digit_matches:
        day = match[:2]
        month = match[2:4]
        year = match[4:]

        if int(year) <= current_year_short:
            full_year = "20" + year
        else:
            full_year = "19" + year
        found_dates.add(f"{day}{month}{year}")
        found_dates.add(f"{day}{month}{full_year}")

    date_matches = re.findall(r'(\d{1,2})[\.\-/](\d{1,2})[\.\-/](\d{2,4})', text)
    for d, m, y in date_matches:
        day = d.zfill(2)
        month = m.zfill(2)
        if len(y) == 2:
            y = "20" + y if int(y) <= current_year_short else "19" + y
        found_dates.add(f"{day}{month}{y}")
        found_dates.add(f"{y}{month}{day}")

    word_date_matches = re.findall(r'(\d{1,2})\s+([a-zA-Zа-яА-Я]+)\s+(\d{2,4})', text, flags=re.IGNORECASE)
    for d, m, y in word_date_matches:
        day = d.zfill(2)
        for key, values in MONTHS.items():
            if m.lower() in map(str.lower, values):
                month_abbr = key.upper()
                if len(y) == 2:
                    y = "20" + y if int(y) <= current_year_short else "19" + y
                found_dates.add(f"{day}{month_abbr}{y}")
                found_dates.add(f"{y}{month_abbr}{day}")
                
    word_date_matches_2 = re.findall(r'([a-zA-Zа-яА-Я]+)\s+(\d{1,2})\s+(\d{2,4})', text, flags=re.IGNORECASE)
    for m, d, y in word_date_matches_2:
        day = d.zfill(2)
        for key, values in MONTHS.items():
            if m.lower() in map(str.lower, values):
                month_abbr = key.upper()
                if len(y) == 2:
                    y = "20" + y if int(y) <= current_year_short else "19" + y
                found_dates.add(f"{day}{month_abbr}{y}")
                found_dates.add(f"{y}{month_abbr}{day}")

    return list(found_dates)