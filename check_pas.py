import hashlib
import requests
from typing import Optional

def pwned_api_check(password: str) -> int:
    if not password:
        raise ValueError("Password cannot be empty")
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]

    try:
        headers = {'User-Agent': 'Python-PwnedPasswordChecker'}
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code != 200:
            raise RuntimeError(f"API error: Status code {response.status_code}")
        for line in response.text.splitlines():
            hash_part, count = line.split(':')
            if hash_part == suffix:
                return int(count)
        return 0

    except requests.RequestException as e:
        raise RuntimeError(f"Failed to connect to API: {str(e)}")
