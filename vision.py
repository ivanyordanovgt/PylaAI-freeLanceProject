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
            'detectGameStart': self.detectGameStart,

        }
        self.enemyCoords = []
        self.show_count = 0
        self.findMinions = 'detectMinions'
        self.findChampions = 'detectChampions'

        keyboard.on_press_key("x", lambda _: self.__turn_of_bot())

    def loadImages(self):
        self.shopImage = cv2.imread('images/shop.JPG')
        self.mageMinion = cv2.imread('images/mageMinion.JPG')
        self.mageMinion2 = cv2.imread('images/mageMinion2.JPG')
        self.mageMinion4 = cv2.imread('images/mageMinion4.JPG')
        self.meleMinion = cv2.imread('images/fighterMinion.JPG')
        self.meleMinion2 = cv2.imread('images/fighterMinion2.JPG')
        self.meleMinion3 = cv2.imread('images/fighterMinion3.JPG')
        self.Button = cv2.imread('images/acceptBtn.JPG')

        self.xBtn = cv2.imread('images/xBtn.JPG')
        self.okBtn = cv2.imread('images/okBtn.JPG')
        self.arrowBtn = cv2.imread('images/arrowBtn.JPG')
        self.continueBtn = cv2.imread('images/continueBtn.JPG')
        self.playAgainBtn = cv2.imread('images/playAgainBtn.JPG')


    def recall(self):
        time.sleep(0.5)
        startY = 640
        endY = 680
        startX = 927
        endX = 980

        self.click(1300, 900, r=True)
        time.sleep(8)
        os.startfile('b.ahk')
        time.sleep(8.8)
        self.buyItems()
        self.lastRecall = time.time()

    def findAllyMinions(self):
        threshold = 0.5
        result = self.findImage(self.mageMinion, threshold), \
                 self.findImage(self.mageMinion2, threshold), \
                 self.findImage(self.mageMinion4, threshold), \
                 self.findImage(self.meleMinion, threshold), \
                 self.findImage(self.meleMinion2, threshold), \
                 self.findImage(self.meleMinion3, threshold)

        resultBooleans = [x[0] for x in result]
        minionCoords = [x[1] for x in result]
        print('minion coords', minionCoords[0])
        for coords in minionCoords:
            for pt in zip(*coords[::-1]):  # Switch collumns and rows
                if pt[0] - 10 > self.playerCoords[0]:
                    # print(pt[0], self.playerCoords[0])
                    print('MINION IS IN FRONT')
                    return True
        # if True in resultBooleans:
        #     print('FOUND MINION', random.randint(1, 10000))
        #     return True
        return False

    @staticmethod
    def click(x, y, click=False, l=False, r=False):
        win32api.SetCursorPos((x, y))

        if l:
            try:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            except:
                """
                Sometimes win32api throws an error without any message
                for no reason so we have to catch the error
                """
                pass
        if r:
            try:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
            except:
                pass


    def buyItems(self):
        keyboard.startfile('p.ahk')
        time.sleep(0.3)
        self.click(809, 500, click=True, l=True)
        pyautogui.rightClick()
        pyautogui.rightClick()
        mouse.right_click()
        time.sleep(0.3)
        os.startfile('p.ahk')
        time.sleep(0.1)
        self.command = 'play'

    def detectGameStart(self):
        print("?")
        resultBoolean, loc = self.findImage(self.shopImage, threshold=0.7)
        if not resultBoolean:
            result, _ = self.findImage(self.acceptButton, threshold=0.7)
            if result is True:
                return 'break'
            time.sleep(0.5)
            return
        print('found shop!')
        self.buyItems()
        self.command = 'goToLane'

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
