import pyautogui
import time
import math

# от замеренного времени откладываем три секунды до запуска программы
begin_time = time.time()
time.sleep(3)
ww = 480
screen = pyautogui.screenshot(region=(0, 565, 1500, 150))  # делаем снимок области
fly = 0
number = 0

while True:
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
                break

    ti = time.time() - begin_time
    if ti < 150:
        ww = 5 * ti + 480
    elif fly == 1:
        time.sleep(0.2)
        for x in range(60, 100):
            if current_colour == screen.getpixel((x, 110)):
                fly = 0
                break
        if fly == 1:
            pyautogui.keyDown('DOWN')
            time.sleep(0.015)
            pyautogui.keyUp('DOWN')
            fly = 0
