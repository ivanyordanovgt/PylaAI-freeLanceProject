import os

import mouse
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import numpy as np
import win32con
import cv2
from pynput.keyboard import Key, Controller


import os

import mouse
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import numpy as np
import win32con
import cv2
from extractText import extractText
from pynput.keyboard import Key, Controller
class Pyla:

    def __init__(self):

        self.command = 'nothing'
        self.game_image = None
        self.inGame = True
        self.original_image = None
        self.AI = {
            'nothing': lambda: True,
        }
        self.enemyCoords = []
        self.show_count = 0
        self.findMinions = 'detectMinions'
        self.findChampions = 'detectChampions'

        keyboard.on_press_key("x", lambda _: self.__turn_of_bot())


    def AIcontroller(self, game_image=None):
        click_coords = []
        start_y, end_y = 120, 880
        start_x, end_x = 420, 1370
        self.original_image = game_image
        game_image = game_image[start_y + 80:end_y - 250, start_x:end_x]
        self.game_image = game_image

        command = self.AI[self.command]()
        cv2.drawMarker(game_image, (450, 330), (0, 0, 255), cv2.MARKER_STAR, thickness=4)
        # cv2.imshow('Bot finder', self.game_image)
        print(self.command)
        time.sleep(0.2)
        return command
