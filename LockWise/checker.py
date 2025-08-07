from colorama import Fore, Style
from colorama import init
init(autoreset=True)
import re
import math
import hashlib
import requests

def is_password_pwned(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    try:
        response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
        if response.status_code != 200:
            raise Exception("API error")

        hashes = (line.split(':') for line in response.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return int(count)
        return 0

    except Exception:
        return -1  # API failed

def load_common_passwords(filepath="common.txt"):
    try:
        with open(filepath, "r") as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        return set()

def calculate_entropy(password):
    charset = 0
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(not c.isalnum() for c in password):
        charset += 33
    if charset == 0:
        return 0.0
    entropy = math.log2(charset) * len(password)
    return round(entropy, 2)

def evaluate_password(password, common_passwords):
    feedback = []
    score = 0

    pwned_count = is_password_pwned(password)
    if pwned_count > 0:
        feedback.append(f"{Fore.RED}This password has been found in data breaches. Do NOT use it.{Style.RESET_ALL}")
        score = 0
    elif pwned_count == -1:
        feedback.append(f"{Fore.YELLOW}Could not verify against breach database (API failed).{Style.RESET_ALL}")

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append(f"{Fore.RED}Make your password at least 8 characters long.{Style.RESET_ALL}")

    # Case checks
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append(f"{Fore.RED}Add at least one uppercase letter.{Style.RESET_ALL}")
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append(f"{Fore.RED}Add at least one lowercase letter.{Style.RESET_ALL}")

    # Digit check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append(f"{Fore.RED}Add at least one digit.{Style.RESET_ALL}")

    # Special character check
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
    else:
        feedback.append(f"{Fore.RED}Add at least one special character (!@#$%^&*).{Style.RESET_ALL}")

    # Common password check
    if password.lower() in common_passwords:
        feedback.append(f"{Fore.RED}This is a commonly used password. Avoid using it.{Style.RESET_ALL}")
        score = 0

    entropy = calculate_entropy(password)

    if score >= 6 and entropy > 60:
        strength = f"{Fore.GREEN}Strong{Style.RESET_ALL}"
    elif score >= 4 and entropy > 40:
        strength = f"{Fore.YELLOW}Moderate{Style.RESET_ALL}"
    else:
        strength = f"{Fore.RED}Weak{Style.RESET_ALL}"

    return strength, feedback, entropy, pwned_count