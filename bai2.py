import pyautogui as pag
import time 

image = 'HinhAnh/setting.png'
loc = pag.locateOnScreen(image) # chỉ định hình để click
pag.click(loc) #click vào hình ảnh setting.png