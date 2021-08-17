"""
Press Ctrl+C to exit script
"""

import pyautogui

# focus on game screen
pyautogui.click(1,1)
pyautogui.sleep(0.5)

def key_press(key):
	pyautogui.keyDown(key)
	pyautogui.keyUp(key)
	pyautogui.sleep(0.5)

# press multiple keys at the same time
def cmb_keys(k1, k2):
	pyautogui.keyDown (k1) 
	pyautogui.keyDown (k2) 
	pyautogui.sleep(0.5)
	pyautogui.keyUp (k2) 
	pyautogui.keyUp (k1) 
	pyautogui.sleep(0.5)

def confirm():
	cmb_keys('shift', 'enter')

def move_cursor_down():
	key_press('down')

def move_left():
	pyautogui.keyDown('a') 
	pyautogui.sleep(0.5)
	pyautogui.keyUp('a') 

def move_right():
	pyautogui.keyDown('d') 
	pyautogui.sleep(0.5)
	pyautogui.keyUp('d') 	
	
def escape():
	key_press('esc')

def turn_in_loop():
	confirm() # enter inventory
	confirm() # confirm cookie
	confirm() # handover
	confirm() # say yes
	confirm() # dialog box
	confirm() # HQ dialog box
	confirm() # complete
	
def take_leve():
	cmb_keys('ctrl', 'f1') # target Eirikur
	confirm() # start chatting with Eirikur
	confirm() # enter leve selection
	move_cursor_down() # move to trade leve
	confirm() # select trade leve
	confirm() # select cookie leve
	confirm() # confir, selection of cookie leve
	escape() # exit leve selection
	escape() # exit converstaion w/ Eirikur
	# move right to turn in leve
	move_right()
	turn_in_leve()

def turn_in_leve():
	cmb_keys('ctrl', 'f1') # target Moyce
	confirm() # enter leve turn-in selection
	move_cursor_down() # move to trade leve
	move_cursor_down() # move to trade leve
	confirm() # confirm selection
	confirm() # enter turn in
	# loop
	turn_in_loop() # round 1 turn in
	confirm() # confirm enter round 2
	confirm() # confirm enter round 2
	turn_in_loop() # round 2 turn in
	confirm() # confirm enter round 3
	confirm() # confirm enter round 3
	turn_in_loop() # round 3 turn in
	# move left to take leve
	move_left()
	
while True:
	take_leve()