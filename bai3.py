import pyautogui as pag
import time

time.sleep(5)
for i in range(3): # thay bằng while True: để chạy vô hạn
    pos = pag.position(1033,521)
    pag.doubleClick(pos)
    time.sleep(3)

    pos2 = pag.position(1864,615)
    pag.click(pos2)
    time.sleep(3)
