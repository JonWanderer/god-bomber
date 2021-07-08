import os, time, sys,sms, call
from termcolor import colored



def slowprint(s):
    for c in s + '\n' :
        print(c, end="")
        time.sleep(1. / 100)

def updatefirst():
    os.system("cd && rm -rf ~/.gb && sed -i '/alias godbomber/d' ~/../usr/etc/bash.bashrc")

def update():
				a=input("Вы уверены, что хотите обновить? (y/n) ")
				if a=="y":
					os.system("curl https://raw.githubusercontent.com/lkqas/god-bomber/master/install.sh | sh && exec bash")
					exit()
				else:
					print("Отменено")

def main():
    os.system("clear")
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
        updatefirst
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