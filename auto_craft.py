"""
Press Ctrl+C to exit script
"""

import pyautogui

#pyautogui.mouseInfo()

# focus on game screen
pyautogui.click(1150,614)
pyautogui.sleep(2)

#mouse method
"""
while True:
	pyautogui.moveTo(1285,749)
	pyautogui.click(clicks=2, interval=0.25)
	pyautogui.sleep(2)

	pyautogui.moveTo(1707,935)
	pyautogui.click(clicks=2, interval=0.25)
	pyautogui.sleep(2)
"""

# start synthesizing
def synthesis():
	pyautogui.keyDown ('shift') 
	pyautogui.keyDown ('enter') 
	pyautogui.sleep(0.5)
	pyautogui.keyUp ('enter') 
	pyautogui.keyDown('enter')
	pyautogui.sleep(0.5)
	pyautogui.keyUp ('enter') 
	pyautogui.keyUp ('shift') 
	pyautogui.sleep(0.5)
	crafting_macro()

# press macro - ctrl+b is the keybind of my crafting macro
def crafting_macro():
	pyautogui.keyDown ('ctrl') 
	pyautogui.keyDown ('b') 
	pyautogui.sleep(0.5)
	pyautogui.keyUp ('b') 
	pyautogui.keyUp ('ctrl') 
	pyautogui.sleep(40)

# keyboard method
while True:
	pyautogui.moveTo(1285,749) # focus on game screen
	pyautogui.click()
	synthesis()