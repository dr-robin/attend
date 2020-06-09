#!/usr/bin/env python3

import subprocess
import pyautogui
import webbrowser

#Open discord
subprocess.call(["discord"])

#Maximise current window
pyautogui.press(["alt", "F10"])

#switch discord server
pyautogui.press(["ctr", "2"])
print("don't forget to join the general voice channel")

#Open my.becode
webbrowser.open('https://my.becode.org/dashboard')
pyautogui.press(["F5"])
print("don't forget to click attendence time")
