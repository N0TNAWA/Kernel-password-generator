import os
import time
import random
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
    Choices = input('''
    1: Generate passwords
    2: Clear password list
    > ''')

    if Choices == '1':
        print(Fore.RED + 'Press enter to use default directory/Saved-passwords.txt')
        print(Fore.RED + 'Press ctrl+c to stop generating.')
        directory = input(Fore.RED + 'Where do you wanna save the passwords?... ')
        file_path = directory
        if file_path:
            pass
        else:
            file_path = 'Saved-passwords.txt'
        length1 = int(input(Fore.RED + 'How long do you want the passwords to be?... '))

        length2 = length1
        amount = 1

        os.system('cls')

        while True:
            for x in range(amount):
                password = "".join(random.sample(all, length2))
                print(Fore.LIGHTGREEN_EX + password)
                with open(file_path, 'a') as path:
                    path.write(password)
                    path.write("\n")
                    path.close()

    elif Choices == '2':
        directory = input(Fore.RED + 'What text file do you wanna wipe?... ')
        file_path = directory
        if file_path == directory:
            pass
        elif file_path != directory:
            print(Fore.YELLOW + 'Invalid text file')
            time.sleep(2)
            os.system('cls')
            main()

        amount = 0

        with open(file_path, 'r') as path:
            for line in path:
                amount = amount + 1
                print(f'Passwords: {amount}, Content: {line.rstrip()}, Location: {file_path}')

            path.close()
            Sure = ''
            while Sure not in ['Yes', 'yes', 'Y', 'y', 'No', 'no', 'N', 'n']:
                Sure = input(Fore.RED + f'All {amount} passwords have been checked. Are you sure you wanna delete these possible passwords?... Y/N ')

            if Sure == 'Yes' or Sure == 'yes' or Sure == 'Y' or Sure == 'y':
                with open(file_path, 'w'):
                    print(f'Passwords Deleted: {amount}, Location: {file_path}')
                    os.system('cls')
                    main()

            elif Sure == 'No' or Sure == 'no' or Sure == 'N' or Sure == 'n':
                os.system('cls')
                main()


if __name__ == '__main__':
    os.system('cls')
    main()