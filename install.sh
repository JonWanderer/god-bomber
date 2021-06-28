apt update
apt upgrade
apt install -y git python
pip install GitPython
pip install requests termcolor GitPython
git clone https://github.com/lkqas/god-bomber ~/.gb
echo 'alias godbomber="python ~/.gb/godbomber.py"' >> ~/../usr/etc/bash.bashrc
echo "GodBomber установлен!"
