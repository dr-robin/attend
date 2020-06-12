#!/usr/bin/env python3
import subprocess
import pyautogui
import webbrowser

#Open my.becode
webbrowser.open('https://my.becode.org/dashboard')
pyautogui.press(["F5"])  #refresh webpage
pyautogui.press(["alt", "F10"]) #maximise screen
pyautogui.press(["ctr", "f"])  #find time
pyautogui.write("09:00")
pyautogui.press(["enter"])
pyautogui.click(314, 498, clicks=1,duration=10)  #mouseclick

#Open discord
subprocess.call("/usr/bin/discord")
pyautogui.press(["alt", "F10"]) #Maximise current window
pyautogui.press(["ctr", "2"])  #switch discord server

#Make pop-up reminder window
import tkinter
window = tkinter.Tk()
# to rename the title of the window
window.title("WARNING ATTENDANCE CHECK")
# pack is used to show the object in the window
label = tkinter.Label(window, text = "Don't forget to check your attendance at my.becode.org").pack()
window.mainloop()
