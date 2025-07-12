"""
This script automates the process of opening URLs from a JSON file in a web browser,
selecting the URL in the address bar, and printing the page.

Since the website is protected by a cloudflare bot protection, the script uses
pynput to control the mouse and keyboard to interact with the browser.

Web scraping is done by simulating user actions, such as clicking and typing,
other than using traditional scraping libraries since the website is protected.

"""

from pynput.mouse import Controller as MouseController
from pynput.mouse import Button
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key
import time
import json

mouse = MouseController()
keyboard = KeyboardController()

urls = json.load(open('scrapped_urls.json'))[76:]

time_interval = 0.4
print("Starting in 3")
time.sleep(time_interval)
print("Starting in 2")
time.sleep(time_interval)
print("Starting in 1")
time.sleep(time_interval)


def write_text(text):
    for char in text:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.01)  


for url in urls:
    mouse.position = (509, 59)
    time.sleep(0.01)
    mouse.click(Button.left, 1)
    time.sleep(time_interval)

    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.ctrl)

    
    write_text(url)
    
    time.sleep(time_interval)
    
    keyboard.press(Key.enter)
    
    time.sleep(2)  

    keyboard.press(Key.ctrl)
    keyboard.press('p')
    keyboard.release('p')
    keyboard.release(Key.ctrl)

    time.sleep(4)

    mouse.position = (1457, 903)
    time.sleep(0.01)
    mouse.click(Button.left, 1)

    time.sleep(1)

    mouse.position = (782, 500)
    time.sleep(0.01)
    mouse.click(Button.left, 1)

    time.sleep(2)
