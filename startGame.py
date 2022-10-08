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


class PylaStart:

    def __init__(self, state):
        self.clickCount = 0
        self.pickChampionCommandTries = 0
        self.progressState = 'find'
        self.originalImage = None
        # self.progressState = 'findNewGame'
        self.playBtn = cv2.imread('images/playBtn.JPG')
        self.confirmBtn = cv2.imread('images/confirmBtn.JPG')
        self.findMatchBtn = cv2.imread('images/findMatch.JPG')
        self.acceptBtn = cv2.imread('images/acceptBtn.JPG')
        self.lockInBtn = cv2.imread('images/lockIn.JPG')
        self.shopImage = cv2.imread('images/shop.JPG')

        self.xBtn = cv2.imread('images/xBtn.JPG')
        self.okBtn = cv2.imread('images/okBtn.JPG')
        self.arrowBtn = cv2.imread('images/arrowBtn.JPG')
        self.continueBtn = cv2.imread('images/continueBtn.JPG')
        self.playAgainBtn = cv2.imread('images/playAgainBtn.JPG')
        self.bigOkBtn = cv2.imread('images/bigOkBtn.JPG')
        self.championOptions = {
            'sona': cv2.imread('images/sona.JPG'),
            'twitch': cv2.imread('images/twitch.JPG'),
            'cait': cv2.imread('images/cait.JPG'),
            'miss': cv2.imread('images/cait.JPG'),
            'garen': cv2.imread('images/Garen.JPG'),
            'tryndamere': cv2.imread('images/tryndamere.JPG'),
            'yi': cv2.imread('images/masterYi.JPG'),
        }
        self.pickChampionTries = 0
        self.tryToFindChampionMaxCycles = 6
        self.championIndex = 0
        self.screenshot = None
        self.tries = 0
        self.bonusX = 570
        self.bonusY = 310
        self.champBonus = 60    

        self.startGameOptions = {
            'start': lambda: self.__look_for_template(self.screenshot, self.playBtn, 'confirm'),
            'confirm': lambda: self.__look_for_template(self.screenshot, self.confirmBtn, 'find'),
            'find': lambda: self.__look_for_template(self.screenshot, self.findMatchBtn, 'accept',
                                                     onSuccess='Pressed find match',
                                                     onError='Trying to locate find match'),
            'accept': lambda: self.__look_for_template(self.screenshot, self.acceptBtn, 'pickChampion',
                                                       onSuccess='Accepted match.',
                                                       onError='Waiting to accept to show up', threshold=0.5,
                                                       bonusX=self.bonusX - 50, bonusY=self.bonusY - 20),
            'pickChampion': lambda: self.pickChampion('Picked champion', 'Looking for champions to pick..'),
            'lockIn': lambda: self.__look_for_template(self.screenshot, self.lockInBtn, 'detectGameStart',
                                                       onSuccess='Locked in champion',
                                                       onError='Trying to lock in...',
                                                       bonusX=self.bonusX,
                                                       bonusY=self.bonusY),
            'detectGameStart': lambda: self.detectGameStart(),
            'findNewGame': lambda: self.findNewGame(),
            'end': lambda: print('Game detected lets play!'),  # This message doesn't matter it won't be used anywhere

        }

    def __look_for_template(self, image, template, progressState=None, threshold=0.7, onSuccess=None, onError=None,
                            static=False,
                            bonusX=None, bonusY=None, dontClick=False, clickAway=False):
        if bonusX:
            bonusX = bonusX
            bonusY = bonusY
        else:
            bonusX = self.bonusX
            bonusY = self.bonusY  # Default readjusting
        x, y = self.findImageInClient(image, template)
        if x:
            time.sleep(0.3)
            if static:
                if not dontClick:
                    self.click(x + bonusX, y + bonusY, l=True)
                    if clickAway:
                        time.sleep(0.1)
                        self.click(400, 350)
                        time.sleep(3)
                return True
            self.click(x + bonusX, y + bonusY, l=True)
            self.progressState = progressState
            return onSuccess
        return onError     

    def click(x, y, l=False, r=False):
        win32api.SetCursorPos((x, y))

        if l:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        if r:
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        time.sleep(0.1)

    def start(self, image):
        self.originalImage = image
        image = image[240:870, 450:1300]
        self.screenshot = image
        time.sleep(0.1)
        return message
