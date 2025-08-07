import getpass
from checker import evaluate_password, load_common_passwords
from colorama import Fore, Style
from banner import display_banner

def main():
    display_banner()
    print("\n🔐 Password Strength Checker")
    print("------------------------------------")

    common_passwords = load_common_passwords("common.txt")

    while True:
        password = input("\nEnter a password to check: ")

        strength, feedback, entropy, pwned_count = evaluate_password(password, common_passwords)

        print("\n Password Strength:", strength)
        print(" Entropy:", entropy, "bits")

        if pwned_count > 0:
            print(f"{Fore.RED}  This password was found {pwned_count} times in data breaches (source: online API).{Style.RESET_ALL}")
        elif pwned_count == 0:
            print(f"{Fore.GREEN}  This password was not found in known breaches.{Style.RESET_ALL}")
        elif pwned_count == -1:
            print(f"{Fore.YELLOW}  Unable to verify breach status (API request failed).{Style.RESET_ALL}")

        if feedback:
            print(f"\n{Fore.WHITE}Suggestions to improve your password:{Style.RESET_ALL}")
            for tip in feedback:
                print("-", tip)

        again = input("\nDo you want to check another password? (y/n): ").lower()
        if again != 'y':
            print("Exiting Password Strength Checker. Stay secure!")
            break

if __name__ == "__main__":
    main()