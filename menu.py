import os
import time
import sys
from colorama import Style, Back, Fore
from termcolor import colored


def main():
    os.system("cls")
    os.system("clear")
    print(colored('''
       
{Fore.BLUE}Выберите пункт:
{Fore.BLUE}1.{Style.RESET_ALL} sms-bomb
{Fore.BLUE}2.{Style.RESET_ALL} call-bomb
{Fore.BLUE}3.{Style.RESET_ALL} обновление.
{Fore.BLUE}4.{Style.RESET_ALL} exit/quit
''','red'))

    cmd = input("@ > ")

    if cmd == "1":
        from godbomber import godbomber
    elif cmd == "2":
        print(colored("В разработке!",'red'))
    elif cmd == "3":
        from godbomber import Update
    elif cmd == "4":
        sys.exit()
    else:
        print(f"{Fore.RED}что то пошло не так...{Style.RESET_ALL}")
        time.sleep(3)
        main()
main()