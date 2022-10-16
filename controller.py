import time

import cv2
import keyboard
import numpy as np
from PIL import ImageGrab
import win32gui
import win32ui
import win32con
import tkinter


PylaStart = PylaStart('start')

def play():
    result = ''
    win_cap = WindowCapture()
    while result is not True:
        screenshot = win_cap.get_screenshot()
        result = PylaAI.AIcontroller(screenshot)
    PylaStart.progressState = 'findNewGame'


def start():
    win_cap = WindowCapture()
    cleanInfo = None
    dotCounter = 0
    info = None
    while info is not True:
        screenshot = win_cap.get_screenshot()
        info = PylaStart.start(screenshot)



count = 0


def controlAI():

    while True:
        start()
        play()


controlAI()
print("Exit")
