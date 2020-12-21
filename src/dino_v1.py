import pyautogui
import time
import math

# от замеренного времени откладываем три секунды до запуска программы
begin_time = time.time()
time.sleep(3)
ww = 480
screen = pyautogui.screenshot(region=(0, 565, 1500, 150))  # делаем снимок области

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
                pyautogui.keyDown('SPACE')
                time.sleep(0.01)
                break

    current_time = time.time()
    if current_time - begin_time <= 150:
        ww += 0.375
