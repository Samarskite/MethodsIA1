import pyautogui
import pytweening
import numpy as np
import cv2
import time

pyautogui.click(1350, 1550)
time.sleep(0.5)
vert = 50
hoz = 210
hozstart = 0
hozend = 0
vertstart = 0
vertend = 0
firstx = 0
firsty = 0
colour = 255
pos = 0
imglist = []
image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
image = image[512:1332, 800:2000]
cv2.imwrite("image.png", image)
iamge = cv2.imread('image.png')
side = 'top'
while True:
    while side == 'top':
        while True:
            print(colour)
            if colour == 17:
                hoz += 2
                break                
            else:
                hoz+=1
                colour = image[0][hoz][0]
        hozend = hoz
        colour = 255

        while colour > 50:
            vert += 1
            colour = image[vert][hoz][0]
        vertend = vert
        
        if vertend != 0:
            pyautogui.moveTo(800+hozend, 512)  # moves mouse to X of 100, Y of 200.
            pyautogui.dragTo(800+hozend, 512+vertend, 5, pyautogui.easeOutQuad,button='left')
            pyautogui.moveTo(800+hozend, 512)
            colour = 255
            vert = 50
            vertend = 0
            hoz += 7

    while side == 'bottom':
        vert = 800
        while True:
                #print(colour)
                if colour == 17:
                    hoz += 3
                    break                
                else:
                    hoz+=1
                    colour = image[819][hoz][0]
        hozend = hoz
        colour = 255

        while colour > 50:
            vert -= 1
            colour = image[vert][hoz][0]
            print(vert)
        vertend = vert
        
        if vertend != 0:
            pyautogui.moveTo(800+hozend, 1332)  # moves mouse to X of 100, Y of 200.
            pyautogui.dragTo(800+hozend, 512+vertend, 3, pyautogui.easeOutQuad, button='left')
            pyautogui.moveTo(800+hozend, 1332)
            colour = 255
            vert = 800
            vertend = 0
            hoz += 7
    