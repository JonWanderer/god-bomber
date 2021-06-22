pkg update
pkg install python
pkg install git
git clone https://github.com/lkqas/god-bomber.git
cd god-bomber/
pip install termcolor
pip install requests
python godbomber.py

print("обновление прошло успешно, перезапустите программу.")

sys.exit()
