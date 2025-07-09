import hashlib
import requests

def pwned_api_check(password: str) -> int:
    if not password: # Проверка на наличие введенного пароля
        raise ValueError("Password cannot be empty") 
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() # Шифрование пароля
    prefix, suffix = sha1_hash[:5], sha1_hash[5:] # Взятие нужных частей

    try:
        headers = {'User-Agent': 'Python-PwnedPasswordChecker'} # Определение заголовков
        url = f"https://api.pwnedpasswords.com/range/{prefix}" # Создание ссылки для запроса
        response = requests.get(url, headers=headers, timeout=5) # Запрос на сервер
        if response.status_code != 200: # Проверка ответа и его обработка
            raise RuntimeError(f"API error: Status code {response.status_code}")
        for line in response.text.splitlines(): # Получение количества совпадений
            hash_part, count = line.split(':')
            if hash_part == suffix: # Проверка, что отправленный и полученный пароли совпадают 
                return int(count)
        return 0
    except requests.RequestException as e: # Обработка ошибок
        raise RuntimeError(f"Failed to connect to API: {str(e)}")