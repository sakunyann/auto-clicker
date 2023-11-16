#!/usr/bin/env python3

import pyautogui

#Collect X, Y coordinates for each component:
pyautogui.position()

#Simple click loop with interval: 2 clicks at 0.75 second intervals
for x in range(4):
if x == 3: break
pyautogui.click(clicks=2, interval=0.75)


#Loop clicking over coordinates as well as drag and drop.
for x in range(4):
    if x == 3: break 
    #Moves cursor over coorinates  
    pyautogui.moveTo(478, 942) 
    #2 clicks at 0.75 second intervals	
    pyautogui.click(clicks=2, interval=0.75)

    #Drag and drop
    pyautogui.moveTo(307, 768)
    pyautogui.mouseDown(button=’left’)
    pyautogui.moveTo(322, 672)
    pyautogui.mouseUp(button=’left’)
