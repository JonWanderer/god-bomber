apt update
apt upgrade -y
apt install -y git python
pip install requests termcolor
git clone https://github.com/lkqas/god-bomber ~/.gb
echo 'alias godbomber="python ~/.gb/godbomber.py"' >> ~/../usr/etc/bash.bashrc
echo "GodBomber установлен!"
