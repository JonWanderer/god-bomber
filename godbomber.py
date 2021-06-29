import os, time, sys, sms, call, update
from termcolor import colored


def slowprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.01)

showMenu = True
while showMenu:
    os.system("clear")

    slowprint(colored('''
	┏━━━┳━━━┳━━━┳━━┓┏━━━┳━┓┏━┳━━┓┏━━━┳━━━┓
	┃┏━┓┃┏━┓┣┓┏┓┃┏┓┃┃┏━┓┃┃┗┛┃┃┏┓┃┃┏━━┫┏━┓┃
	┃┃╋┗┫┃╋┃┃┃┃┃┃┗┛┗┫┃╋┃┃┏┓┏┓┃┗┛┗┫┗━━┫┗━┛┃
	┃┃┏━┫┃╋┃┃┃┃┃┃┏━┓┃┃╋┃┃┃┃┃┃┃┏━┓┃┏━━┫┏┓┏┛
	┃┗┻━┃┗━┛┣┛┗┛┃┗━┛┃┗━┛┃┃┃┃┃┃┗━┛┃┗━━┫┃┃┗┓
	┗━━━┻━━━┻━━━┻━━━┻━━━┻┛┗┛┗┻━━━┻━━━┻┛┗━┛
	by @lkqas
	version 0.9

	''','yellow'))
    print(colored('''
Выберите пункт:
1. Sms-bomb
2. Call-bomb
3. Update
4. Quit
5. Credits
''','green'))

    cmd = input("# > ")

    if cmd == "1":
        showMenu = False
        sms.spam()
    elif cmd == "2":
        showMenu = False
        call.spam()
    elif cmd == "3":
        showMenu = False
        update.up()
    elif cmd == "4":
        sys.exit()
    elif cmd == "5":
        print(colored("Devs: flexagoon, lkqas ",'red'))
        print(colored("links: https://t.me/ravvs_archive, https://t.me/lkqas",'blue'))
        time.sleep(10)
    else:
        print(colored("что то пошло не так...",'red'))
        time.sleep(3)
