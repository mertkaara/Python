from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from PIL import Image
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#Alan:
#Sol üst = X:  830 Y:  460      x:830   y:465
#Sağ üst = X: 1329 Y:  470      x:1370  y:465 
#Sağ alt = X: 1370 Y:  999      x:1370  y:1000
#Sol alt = X:  801 Y:  963      x:830   y:1000

#Item isim:
#Sol üst = x:1026 y:667
#Sağ üst = x:1262 y:667 
#Sağ alt = x:1262 y:690
#Sol alt = x:1026 y:690
#(1026,667,236,30)

#envanterdeki item koordinatları = x:942 y:660 648-668
#prefix silme = x:818 y:660
#suffix silme = x:848 y:660
#prefix basma = x:880 y:660
#suffix basma = x:913 y:660
#refine button = x:1201 y:864


random_sleep_time = random.uniform(0.14, 0.26)
random_click_time = random.uniform(0.048, 0.11)
random_bekleme = random.uniform(0.5, 0.9)
def double_click2(x,y):
    pyautogui.doubleClick(x, y)
    

def double_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(random_click_time)    # Kısa bir bekleme süresi
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(random_sleep_time)    # Random bir bekleme süresi
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(random_click_time)    # Kısa bir bekleme süresi
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def item_check():
    while keyboard.is_pressed('q') == False:
        pic = pyautogui.screenshot(region=(1026,667,236,30))
        new_size = (4 * pic.width, 4 * pic.height)
        pic = pic.resize(new_size)
        output = pytesseract.image_to_string(pic)
        output = output.split(' ')
        output = [item.strip() for item in output if item.strip()]
        return output

while keyboard.is_pressed('q') == False:
    win32api.SetCursorPos((942, 660))
    time.sleep(random_bekleme)
    x = item_check()
    print(x[-1])
    if x[-1] not in ('Final', 'Meteo', 'Bio', 'Bandit', 'Max', 'Squire', 'Ultra', 'Silence'):
        time.sleep(random.uniform(0.45, 0.9))
        double_click((random.randint(931,955)),(random.randint(647,668)))   #item
        time.sleep(random_bekleme)
        double_click((random.randint(868,891)),(random.randint(647,668)))   #suffix silme
        time.sleep(random.uniform(0.7, 0.9))
        double_click((random.randint(1183,1214)),(random.randint(859,870))) #refine button
        time.sleep(random_bekleme)
        #double_click((random.randint(1183,1214)),(random.randint(859,870))) #ok button
        #time.sleep(random.uniform(0.7, 0.9))
        double_click((random.randint(931,955)),(random.randint(647,668)))   #item
        time.sleep(random_bekleme)
        double_click((random.randint(901,922)),(random.randint(647,668)))   #suffix basma
        time.sleep(random.uniform(0.4, 0.8))
        double_click((random.randint(1183,1214)),(random.randint(859,870))) #refine button
        time.sleep(random_bekleme)
        #double_click((random.randint(1183,1214)),(random.randint(859,870))) #ok button
        #time.sleep(random_bekleme)
        continue
    break
    
print('Gelen ek:',x[-1])