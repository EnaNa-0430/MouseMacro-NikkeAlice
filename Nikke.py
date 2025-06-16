from pynput.mouse import Listener, Button, Controller
import threading
import time

mouse = Controller()
print("按下鼠标中键触发 按下时间240ms 间隔45ms")

# test
'''
def on_click(x, y, button, pressed):
    if button == Button.middle and pressed:
        print(f"中键按下，在位置：({x}, {y})")

# 启动监听器
with Listener(on_click=on_click) as listener:
    listener.join()
'''


# toggle_state = False
clicking = False

def alice():
    global clicking
    while clicking:
        mouse.press(Button.left)
        time.sleep(0.24) # 按下0.24s
        mouse.release(Button.left)
        time.sleep(0.045) # 间隔0.045s
'''
def auto_click():
    global clicking
    while clicking:
        mouse.click(Button.left)
        time.sleep(0.5)  # 每0.5秒点击一次
'''

def on_click(x, y, button, pressed):
    global clicking
    # global toggle_state
    if button == Button.middle and pressed:
        # toggle_state = not toggle_state
        clicking = not clicking
        if clicking:
            print("✅ 开始自动点击")
            # clicking = True
            threading.Thread(target=alice, daemon=True).start()
        else:
            print("❌ 停止自动点击")
            # clicking = False

with Listener(on_click=on_click) as listener:
    listener.join()
