import pyautogui
import time
import math

# от замеренного времени откладываем три секунды до запуска программы
begin_time = time.time()
time.sleep(3)
screen = pyautogui.screenshot(region=(0, 565, 1700, 150))  # делаем снимок области
ww = 480

while True:

    vix = 0
    jump = 0
    screen = pyautogui.screenshot(region=(0, 565, 1700, 150))  # делаем снимок области

    colour_1 = screen.getpixel((1, 132))
    colour_2 = colour_1
    first = 1
    second = 0
    for x in range(1, 700):
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
    add_view = math.ceil(ww / 6)
    i = math.ceil(ww)

    """y = 5"""
    if vix == 0 and jump == 0:
        for x in range(239, i + add_view):
            if current_colour == screen.getpixel((x, 5)):
                if x <= i:
                    vix = 1
                    pyautogui.keyDown('SPACE')
                    break
                else:
                    jump = 1
                    break

    """y = 70"""
    if vix == 0 and jump == 0:
        for x in range(239, i + add_view):
            if current_colour == screen.getpixel((x, 70)):
                if x <= i:
                    vix = 1
                    pyautogui.keyDown('SPACE')
                    break
                elif current_colour == screen.getpixel((x + 2, 55)):
                    count = 1
                    for k in range(x, x + 120):
                        if screen.getpixel((k, 70)) != screen.getpixel((k + 1, 70)):
                            count += 1
                    if count == 4:
                        vix = 1
                        pyautogui.keyDown('SPACE')
                        break
                    else:
                        jump = 1
                        break

    """y = 110"""
    """if vix == 0 and jump == 0:
        for x in range(239, i + add_view - 100):
            if current_colour == screen.getpixel((x, 110)):
                vix = 1
                pyautogui.keyDown('SPACE')
                break"""

    ti = time.time() - begin_time
    if ti < 150:
        ww = 480 + ti * 5
