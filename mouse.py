#!/usr/bin/env python

import pyautogui
import time
import datetime

KILL_TIME = "17:01:00"


print("Starting...")
prev_x, prev_y = pyautogui.position()
while True:
    pyautogui.move(-1, 0)

    # Wait for 10 second
    time.sleep(10)

    # Move the mouse cursor one pixel to the right
    pyautogui.move(1, 0)
    pyautogui.click()

    #check distance
    x, y = pyautogui.position()
    distance = ((x - prev_x) ** 2 + (y - prev_y) ** 2) ** 0.5
    if distance > 10:
        break
    prev_x, prev_y = x, y

    # check if time out
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_time > KILL_TIME:
        break

print("Exiting...")
