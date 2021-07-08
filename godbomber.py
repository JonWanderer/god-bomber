<<<<<<< HEAD
import os, time, sys,sms, call
=======
import os, time, sys, sms, call, update
>>>>>>> 68647ad299f3d18fada6e68c8b2056450ed07489
from termcolor import colored


def slowprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.01)

<<<<<<< HEAD
def update():
				a=input("Вы уверены, что хотите обновить? (y/n) ")
				if a=="y":
					os.system("cd && rm -rf godbomber && https://github.com/lkqas/god-bomber.git && sh install.sh ")
					exit()
				else:
					print("Отменено")

=======
showMenu = True
while showMenu:
    os.system("clear")
>>>>>>> 68647ad299f3d18fada6e68c8b2056450ed07489

    slowprint(colored('''
	┏━━━┳━━━┳━━━┳━━┓┏━━━┳━┓┏━┳━━┓┏━━━┳━━━┓
	┃┏━┓┃┏━┓┣┓┏┓┃┏┓┃┃┏━┓┃┃┗┛┃┃┏┓┃┃┏━━┫┏━┓┃
	┃┃╋┗┫┃╋┃┃┃┃┃┃┗┛┗┫┃╋┃┃┏┓┏┓┃┗┛┗┫┗━━┫┗━┛┃
	┃┃┏━┫┃╋┃┃┃┃┃┃┏━┓┃┃╋┃┃┃┃┃┃┃┏━┓┃┏━━┫┏┓┏┛
	┃┗┻━┃┗━┛┣┛┗┛┃┗━┛┃┗━┛┃┃┃┃┃┃┗━┛┃┗━━┫┃┃┗┓
	┗━━━┻━━━┻━━━┻━━━┻━━━┻┛┗┛┗┻━━━┻━━━┻┛┗━┛
	by @lkqas
<<<<<<< HEAD
	version 0.10
	''','yellow'))
=======
	version 0.9
>>>>>>> 68647ad299f3d18fada6e68c8b2056450ed07489

	''','yellow'))
    print(colored('''
Выберите пункт:
<<<<<<< HEAD
1.sms-bomb.
2.call-bomb.
3.update.
4.exit.
5.credits.
=======
1. Sms-bomb
2. Call-bomb
3. Update
4. Quit
5. Credits
>>>>>>> 68647ad299f3d18fada6e68c8b2056450ed07489
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
<<<<<<< HEAD
        showMenu = False
        print(colored("Devs flexagoon, lkqas ",'red'))
        print(colored("links: https://t.me/lkqas_manager  ",'blue'))
        sys.exit()
=======
        print(colored("Devs: flexagoon, lkqas ",'red'))
        print(colored("links: https://t.me/ravvs_archive, https://t.me/lkqas",'blue'))
        time.sleep(10)
>>>>>>> 68647ad299f3d18fada6e68c8b2056450ed07489
    else:
        print(colored("что то пошло не так...",'red'))
        time.sleep(3)
