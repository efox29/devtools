#!/usr/bin/env python

import pyautogui
import time


while True:
        pyautogui.move(-1, 0)

        # Wait for 1 second
        time.sleep(10)

        # Move the mouse cursor one pixel to the right
        pyautogui.move(1, 0)
        pyautogui.click()