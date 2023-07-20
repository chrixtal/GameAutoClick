# GameAutoClick
use python to automaticlly press correct item in web game
2023.07.20 initial version.
target web game: http://game.hg0355.com/game/xpg/?from=timeline&isappinstalled=0
Created by Chris Yang
ref:https://www.cc.ntu.edu.tw/chinese/epaper/home/20220920_006203.html
initial source code use chatgpt to generate it.
pip install pyautogui opencv-python opencv-contrib-python keyboard
running in python 3.10.

how to use:
1. make sure the screen size is 1920x1080, if not, you need adjust regionX, regionY parameter.
2. terminate program to control your mouse press "Ctrl" in default.


clickRandom.py
for game:
http://game.hg0355.com/games/Candy-Game/
