from colorama import Fore, Style

def green(text):
    return Fore.GREEN + str(text) + Style.RESET_ALL

def yellow(text):
    return Fore.YELLOW + str(text) + Style.RESET_ALL

def red(text):
    return Fore.RED + str(text) + Style.RESET_ALL
