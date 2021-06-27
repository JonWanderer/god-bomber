import git

def up():
    repo = git.Repo("~/.gb")
    repo.remotes.origin.pull()
    print("Бомбер обновлен!")
