import pyautogui
import random
import keyboard

# 定義起始座標和格子的間隔
start_x, start_y = 777, 325
grid_size = 70

# 往右六格，往下八格
right_steps = 5
down_steps = 7

# 計算目標座標
rightRan = random.randint(0, right_steps)
downRan = random.randint(0, down_steps)
target_x = start_x + (right_steps * rightRan)
target_y = start_y + (down_steps * downRan)

# 在目標座標附近隨機偏移一點，避免總是點擊同一個位置
#target_x += random.randint(-grid_size // 2, grid_size // 2)
#target_y += random.randint(-grid_size // 2, grid_size // 2)

try:
    # 執行點擊動作，直到按下特定按鍵才停止
    while not keyboard.is_pressed('q'):  # 按下 'q' 鍵時，程式停止
        # 計算目標座標
        rightRan = random.randint(0, right_steps)
        downRan = random.randint(0, down_steps)
        target_x = start_x + (grid_size * rightRan)
        target_y = start_y + (grid_size * downRan)
        pyautogui.click(target_x, target_y)
        print(f"點擊座標：({target_x}, {target_y})")  # 將座標資訊輸出到主控台
except KeyboardInterrupt:
    pass  # 如果使用者在控制台輸入Ctrl+C，則退出程式


