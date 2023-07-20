import cv2
import numpy as np
import pyautogui
import keyboard

# 載入要識別的圖片
element_image = cv2.imread("element.png", 0)

# 需要點擊的元素在畫面上的位置
element_position = None
regionX = 525
regionY = 620

# 進行圖片匹配
def find_element_on_screen():
    global element_position
    screen_image = pyautogui.screenshot(region=(525, 620 , 1378, 821))  # 根據實際情況調整螢幕截圖的大小
    screen_image_gray = cv2.cvtColor(np.array(screen_image), cv2.COLOR_RGB2GRAY)
    
    res = cv2.matchTemplate(screen_image_gray, element_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    # 如果相關性超過一個閾值，則認為找到了要點擊的元素
    if max_val > 0.8:
        element_position = (max_loc[0], max_loc[1])

# 模擬點擊滑鼠左鍵
def click_element():
    global element_position
    if element_position is not None:
        x, y = element_position
        pyautogui.click(regionX+x, regionY+y)

# 主循環
while True:
    find_element_on_screen()
    click_element()
    if keyboard.is_pressed('ctrl'):
        break
