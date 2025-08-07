from pyfiglet import Figlet
from termcolor import colored

def show_banner():
    fig = Figlet(font='standard')
    banner_text = fig.renderText('PHISH  DETEKT')
    colored_banner = colored(banner_text, 'red')
    subtitle = colored('A CLI Phishing Link Scanner - Stay Safe Online', 'cyan')

    print(colored_banner)
    print(subtitle)