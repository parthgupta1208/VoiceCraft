
import os
import pyautogui
import time

# Open paint
os.startfile("mspaint.exe")
time.sleep(2) # Adding delay to make sure paint is fully opened

# Maximize paint window
pyautogui.hotkey("winleft", "up")
time.sleep(1)

# Draw square
pyautogui.click(x=100, y=100) # Click at starting point
time.sleep(1)
pyautogui.dragRel(100, 0, duration=0.5) # Draw line to right
pyautogui.dragRel(0, 100, duration=0.5) # Draw line down
pyautogui.dragRel(-100, 0, duration=0.5) # Draw line to left
pyautogui.dragRel(0, -100, duration=0.5) # Draw line up
time.sleep(1)

# Save as png file
pyautogui.hotkey("ctrl", "s")
time.sleep(1)
pyautogui.write("square.png")
time.sleep(1) # Adding delay to make sure "save as type" dialog box appears
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("alt", "f4")
