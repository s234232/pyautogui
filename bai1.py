import pyautogui as pag
import time #thư viện thời gian

#time để chờ đợi
time.sleep(5) #chờ 5 giây để di chuyển chuột đến vị trí cần click

#tìm tọa độ
pos = pag.position() #.position() return tọa độ con chuột
print(pos)

#click
for i in range(2): #click 2 lần
    pag.click(pos)
    time.sleep(3)