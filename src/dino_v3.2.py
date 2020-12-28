import pyautogui
import time
import math
from multiprocessing import Process

begin_time = time.time() + 3
fly = 0
ww = 480


def view_distance():
    global ww
    while time.time() - begin_time < 150:
        ww += 0.375
        time.sleep(0.071)
        print(ww, "view")


def dino_action():
    global fly
    while True:
        print(ww, "act")
        vix = 0
        screen = pyautogui.screenshot(region=(0, 565, 1500, 150))  # делаем снимок области
        colour_1 = screen.getpixel((1, 132))
        colour_2 = colour_1
        first = 1
        second = 0
        for x in range(1, 1500):
            lo_colour = screen.getpixel((x, 132))
            if lo_colour == colour_1:
                first += 1
            else:
                colour_2 = lo_colour
                second += 1
        if first > second:
            current_colour = colour_1
        else:
            current_colour = colour_2

        d = {5, 70, 110}
        for x in range(239, math.ceil(ww)):
            if vix == 1:
                break
            for y in d:
                if current_colour == screen.getpixel((x, y)):
                    vix = 1
                    fly = 1
                    pyautogui.keyDown('SPACE')
                    time.sleep(0.2)
        if fly == 1:
            for x in range(60, 100):
                if current_colour == screen.getpixel((x, 110)):
                    break
            pyautogui.keyDown('DOWN')
            time.sleep(0.02)
            pyautogui.keyUp('DOWN')
            fly = 0


if __name__ == '__main__':
    proc = Process(target=view_distance, args=())
    proc.start()
    proc = Process(target=dino_action, args=())
    proc.start()

