import random
import os
import colorama
from colorama import Fore

os.system("mode con: cols=153 lines=40")


def main():
    Uppercase_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Lowercase_letters = Uppercase_letter.lower()
    digits = "1234567890"
    Symbols = "()[]{},;.:-_*/\?!#"

    upper, lower, nums, syms, = True, True, True, True

    all = ''

    if upper:
        all += Uppercase_letter
    if lower:
        all += Lowercase_letters
    if nums:
        all += digits
    if syms:
        all += Symbols

    length = 40
    amount = 1

    print(Fore.LIGHTGREEN_EX + '''                                                    
                                                    ██ ▄█▀▓█████  ██▀███   ███▄    █ ▓█████  ██▓                                                         
                                                    ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒ ██ ▀█   █ ▓█   ▀ ▓██▒                                                         
                                                   ▓███▄░ ▒███   ▓██ ░▄█ ▒▓██  ▀█ ██▒▒███   ▒██░                                                         
                                                   ▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  ▓██▒  ▐▌██▒▒▓█  ▄ ▒██░                                                         
                                                   ▒██▒ █▄░▒████▒░██▓ ▒██▒▒██░   ▓██░░▒████▒░██████▒                                                     
                                                   ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒░▓  ░                                                     
                                                   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░░ ░░   ░ ▒░ ░ ░  ░░ ░ ▒  ░                                                     
                                                   ░ ░░ ░    ░     ░░   ░    ░   ░ ░    ░     ░ ░                                                        
                                                   ░  ░      ░  ░   ░              ░    ░  ░    ░  ░                                                     
                                                                                                                                                         
 ██▓███   ▄▄▄        ██████   ██████  █     █░ ▒█████   ██▀███  ▓█████▄      ▄████ ▓█████  ███▄    █ ▓█████  ██▀███   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓    ░▒▓███▀▒░▒████▒▒██░   ▓██░░▒████▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░  ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒      ░   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
░░         ░   ▒   ░  ░  ░  ░  ░  ░    ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░    ░ ░   ░    ░      ░   ░ ░    ░     ░░   ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
               ░  ░      ░        ░      ░        ░ ░     ░        ░             ░    ░  ░         ░    ░  ░   ░           ░  ░            ░ ░     ░     
                                                                 ░                                                                                     ''')

    directory = input(Fore.RED + 'Where do you wanna save the passwords?... ')
    file_path = directory

    while True:
        for x in range(amount):
            password = "".join(random.sample(all, length))
            print(Fore.LIGHTGREEN_EX + password)
            with open(file_path, 'a') as path:
                path.write(password)
                path.write("\n")
                path.close()

if __name__ == '__main__':
    main()