import os, time, sys,sms, call
from termcolor import colored

os.system("clear")

def slowprint(s):
    for c in s + '\n' :
        print(c, end="")
        time.sleep(1. / 100)

def update():
				a=input("Вы уверены, что хотите обновить? (y/n) ")
				if a=="y":
					os.system("cd && rm -rf godbomber && https://github.com/lkqas/god-bomber.git && sh install.sh ")
					exit()
				else:
					print("Отменено")


slowprint(colored('''
	┏━━━┳━━━┳━━━┳━━┓┏━━━┳━┓┏━┳━━┓┏━━━┳━━━┓
	┃┏━┓┃┏━┓┣┓┏┓┃┏┓┃┃┏━┓┃┃┗┛┃┃┏┓┃┃┏━━┫┏━┓┃
	┃┃╋┗┫┃╋┃┃┃┃┃┃┗┛┗┫┃╋┃┃┏┓┏┓┃┗┛┗┫┗━━┫┗━┛┃
	┃┃┏━┫┃╋┃┃┃┃┃┃┏━┓┃┃╋┃┃┃┃┃┃┃┏━┓┃┏━━┫┏┓┏┛
	┃┗┻━┃┗━┛┣┛┗┛┃┗━┛┃┗━┛┃┃┃┃┃┃┗━┛┃┗━━┫┃┃┗┓
	┗━━━┻━━━┻━━━┻━━━┻━━━┻┛┗┛┗┻━━━┻━━━┻┛┗━┛
	by @lkqas
	version 0.10
	''','yellow'))

showMenu = True
while showMenu:
    print(colored('''
       
Выберите пункт:
1.sms-bomb.
2.call-bomb.
3.update.
4.exit.
5.credits.
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
        update
    elif cmd == "4":
        sys.exit()
    elif cmd == "5":
        showMenu = False
        print(colored("Devs flexagoon, lkqas ",'red'))
        print(colored("links: https://t.me/lkqas_manager  ",'blue'))
        sys.exit()
    else:
        print(colored("что то пошло не так...",'red'))
        time.sleep(3)