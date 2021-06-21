import os
import time
import sys
from termcolor import colored

def main():
    os.system("clear")
    print(colored('''
       
Выберите пункт:
1.sms-bomb
2.call-bomb
3.update.
4.exit/quit
''','red'))

    cmd = input("# > ")

    if cmd == "1":
         import godbomber
    elif cmd == "2":
        print(colored("в разработке.",'red'))
    elif cmd == "3":
        print(colored("в разработке.",'red'))
    elif cmd == "4":
        sys.exit()
    else:
        print(colored("что то пошло не так...",'red'))
        time.sleep(3)
        main()
main()