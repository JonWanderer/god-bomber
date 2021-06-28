import git
from termcolor import colored
import sys
import requests

def net_check():
    try:
        requests.get('https://www.google.com', verify=True)
    except:
        print(colored("Замечен плохой интернет....",'red'))
        print(colored('Возобновите интернет, и перезайдите в бомбер...','red'))
        sys.exit()

def up():
    net_check()
    repo = git.Repo("~/.gb")
    repo.remotes.origin.pull()
    print("Бомбер обновлен!")
