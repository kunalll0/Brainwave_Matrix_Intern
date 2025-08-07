from pyfiglet import Figlet
from termcolor import colored
def display_banner():
    fig = Figlet(font='epic')
    banner_text = fig.renderText('LOCKWISE')
    colored_banner = colored(banner_text, 'green', attrs=['bold'])
    subtitle = colored('A CLI Password Strength Checker - Evokes Strength and Security', 'yellow', attrs=['bold'])

    print(colored_banner)
    print(subtitle)