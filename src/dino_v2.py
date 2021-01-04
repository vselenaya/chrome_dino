import pyautogui
import time
import math


class DD:
    def __init__(self):
        self.ww = 480
        self.vix = 0
        self.screen = pyautogui.screenshot(region=(0, 565, 1500, 150))
        self.curr_colour = self.screen.getpixel((1, 132))

    def screenshot(self):
        self.screen = pyautogui.screenshot(region=(0, 565, 1500, 150))

    def dino_colour(self):
        colour_1 = self.screen.getpixel((1, 132))
        colour_2 = colour_1
        first = 1
        second = 0
        for x in range(1, 1500):
            lo_colour = self.screen.getpixel((x, 132))
            if lo_colour == colour_1:
                first += 1
            else:
                colour_2 = lo_colour
                second += 1
        if first > second:
            self.curr_colour = colour_1
        else:
            self.curr_colour = colour_2

    def find_hurdle(self):
        d = {5, 70, 110}
        for x in range(239, math.ceil(self.ww)):
            if self.vix == 1:
                break
            for y in d:
                if self.vix == 1:
                    break
                if self.curr_colour == self.screen.getpixel((x, y)):
                    self.vix = 1
                    pyautogui.keyDown('SPACE')
                    break


Dino = DD()
begin_time = time.time()
time.sleep(3)
while True:
    Dino.vix = 0
    Dino.screenshot()
    Dino.dino_colour()
    Dino.find_hurdle()
    current_time = time.time()
    if current_time - begin_time <= 150:
        Dino.ww += 0.375
