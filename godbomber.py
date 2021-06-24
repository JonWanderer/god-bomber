import os, time, sys, sms, call, update
from termcolor import colored

showMenu = true
while showMenu:
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
        showMenu = false
        sms.spam()
    elif cmd == "2":
        showMenu = false
        call.spam()
    elif cmd == "3":
        update.up()
    elif cmd == "4":
        sys.exit()
    else:
        print(colored("что то пошло не так...",'red'))
        time.sleep(3)
