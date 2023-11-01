from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


#shield pos: X:   87 Y:   40 RGB: ( 70,  92, 133)
#energy pos: X:   71 Y:   37 RGB: (104,  26,  24)

def press_keys():
    keyboard.press('8')
    time.sleep(random.uniform(0.2, 0.6))  # Rastgele bekleme süresi
    keyboard.release('8')
    time.sleep(random.uniform(0.5, 0.9))  # Rastgele bekleme süresi
    keyboard.press('9')
    time.sleep(random.uniform(0.2, 0.7))  # Rastgele bekleme süresi
    keyboard.release('9')
    time.sleep(random.uniform(0.4, 0.8))  # Rastgele bekleme süresi


print(pyautogui.pixel(90,42)[0])
while keyboard.is_pressed('u') == False:
    time.sleep(0.01)
    if pyautogui.pixel(90,42)[0] in range(75, 95):
        time.sleep(0.01)
        continue
    else:
        press_keys()
