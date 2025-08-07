# === main.py ===
from scanner import scan_url
from report import log_report
from colorama import Fore, Style
from banner import show_banner

def main():
    show_banner()  
    while True:
        url = input(Fore.WHITE + Style.NORMAL + "\nEnter a URL to scan: ")
        result = scan_url(url)
        log_report(url, result) 

        again = input("\nDo you want to scan another URL? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print( Fore.WHITE + Style.NORMAL + "\nExiting scanner. Stay safe!")
            break

if __name__ == "__main__":
    main()