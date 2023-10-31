import keyboard
import win32api, win32con
import pyautogui
import time
import random

random_sleep_time = random.uniform(0.2, 0.3)
random_click_time = random.uniform(0.05, 0.1)
random_bekleme = random.uniform(0.1, 0.2)

def double_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(random_click_time)    # Kısa bir bekleme süresi
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(random_sleep_time)    # Random bir bekleme süresi
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(random_click_time)    # Kısa bir bekleme süresi
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

while keyboard.is_pressed('q') == False:
        time.sleep(random.uniform(0.2, 0.4))
        double_click(942,660)   #item
        time.sleep(random_bekleme)
        double_click(818,660)   #prefix silme
        time.sleep(random.uniform(0.2, 0.4))
        double_click(1201,864)  #refine button
        time.sleep(random_bekleme)
        double_click(1201,864)  #ok button
        time.sleep(random.uniform(0.3, 0.5))