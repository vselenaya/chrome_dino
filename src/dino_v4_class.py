import pyautogui
import time
import math


class chrome_dino:
    def __init__(self, based):
        self.vix = False  # показатель, что не надо что-либо делать
        self.begin_time = time.time()

        self.first_screenshot = pyautogui.screenshot()
        self.length = self.first_screenshot.size[0]
        self.height = self.first_screenshot.size[1]
        self.background_colour = self.first_screenshot.getpixel(((self.length // 2), (self.height * 6 // 7)))
        if self.background_colour == (0, 0, 0):
            self.main_colour = (172, 172, 172)
        else:
            self.main_colour = (83, 83, 83)

        self.sc_y1 = math.ceil(565 * self.height / 1080)
        self.sc_x2 = math.ceil(1700 * self.length / 1920)
        self.sc_y2 = math.ceil(150 * self.height / 1080)

        self.view_distance = math.ceil(480 * (self.length / 1920))
        self.screen = pyautogui.screenshot(region=(0, self.sc_y1, self.sc_x2, self.sc_y2))
        self.base = based - math.ceil(565 * self.height / 1080)
        self.current_colour = self.main_colour
        self.add_view = self.view_distance // 6  # добавочная область обзора, см. find_hurdle
        self.time_coefficient = 4.9 * self.length / 1920

        self.sc700 = math.ceil(700 * self.length / 1920)
        self.sc239 = math.ceil(239 * self.length / 1920)
        self.sc5 = math.ceil(5 * self.height / 1080)
        self.sc70 = math.ceil(70 * self.height / 1080)
        self.sc55 = math.ceil(55 * self.height / 1080)
        self.sc120 = math.ceil(120 * self.height / 1080)

    def view_area(self):
        # области обзора зависят линейно от времени работы программы, что подается на вход в функцию
        duration = time.time() - self.begin_time
        if duration < 150:
            self.view_distance = math.ceil(math.ceil(480 * (self.length / 1920)) + duration * self.time_coefficient)
            self.add_view = math.ceil(self.view_distance / 6)

    def screenshot(self):
        self.screen = pyautogui.screenshot(region=(0, self.sc_y1, self.sc_x2, self.sc_y2))

    def dino_colour(self):
        # из-за кочек и ям за цвет динозавра не удастся взять конкретный пиксель основания,
        # потому надо искать самый частый цвет в полосе основания (т.к. ям и кочек не слишком много, чтобы изменить его)
        # благо в основании всего два цвета

        colour_1 = self.screen.getpixel((1, self.base))
        colour_2 = colour_1
        first = 1
        second = 0
        for x in range(1, self.sc700):
            lo_colour = self.screen.getpixel((x, self.base + 1))
            if lo_colour == colour_1:
                first += 1
            else:
                colour_2 = lo_colour
                second += 1
        if first > second:
            self.current_colour = colour_1
        else:
            self.current_colour = colour_2

    def find_hurdle(self):
        # тут у нас есть две области обзора:
        # одна обычная- view_distance (красная на рисунке): что-то попало- немедленнно прыгаем
        # вторая добавочная- view_distance + add_view (розовая/зеленая на рисунке):
        # если там маленький кактус- прыгаем, чтобы приземлиться ближе,
        # если большой кактус/высокий птеродактиль- ничего не делаем, чтобы не влететь в препятствие
        # для определения расстояния смотрим на первое вхождение цвета динозавра-препятствия в строку

        """y = 5, т.е. обзор наверху"""
        # тут установка та же: что-то есть в view_distance- прыгаем
        # если нет, определяем, что в добавочной области: высокий кактус/высокий птеродактиль или же пустота
        # если высокий кактус/высокий птеродактиль, то ничего не делаем (vix = True, чтобы след. цикл не работал)
        # и ждем, когда препятствие попадет в обычную область обзора- тогда и перепрыгнем
        # так мы не тратим драгоценнное время на просчет всего остального
        # а если пустота, просто переходим к след. циклу

        if not self.vix:
            for x in range(self.sc239, self.view_distance + self.add_view):
                if self.current_colour == self.screen.getpixel((x, self.sc5)):
                    if x <= self.view_distance:
                        pyautogui.keyDown('SPACE')
                    self.vix = True
                    break

        """y = 70, или же обзор снизу"""
        # что-то есть в view_distance- прыгаем
        # если нет, то смотрим на добавочную область, тут все сложнее:
        # если там тоже ничего- ура, можно отдохнуть, а если есть, то поймем, что пред нами:
        # данная полоса 70 пересекает разные препятствия по-разному- смотрим на пересечение
        # для начала отличим маленький кактус от группы маленьких кактусов:
        # смотрим на последующие 70 пикселей после первого вхождения по порядку (желтая полоса на рисунке):
        # смотрим на количества переходов из одного цвета в другой: у маленького кактуса их 4, у группы кактусов >4
        # потому находим, что перед нами и прыгаем, если кактус маленький
        # теперь отличим птеродактиля от маленького(-их) кактуса(-ов):
        # птеродактиль машет крыльями, поэтому посмотрим на цвет пикселя справа вверху на заданном
        # в коде расстоянии от исходного: если совпадает с цветом препятствия- кактус(-ы), если нет- птеродактиль
        # итого: маленький кактус- прыгаем, группа маленьких кактусов или птеродактиль- не прыгаем

        if not self.vix:
            for x in range(self.sc239, self.view_distance + self.add_view):
                if self.current_colour == self.screen.getpixel((x, self.sc70)):
                    if x <= self.view_distance:
                        self.vix = True
                        pyautogui.keyDown('SPACE')
                        break
                    elif self.current_colour == self.screen.getpixel((x + 2, self.sc55)):
                        count = 1
                        for k in range(x, x + self.sc120):
                            if self.screen.getpixel((k, self.sc70)) != self.screen.getpixel((k + 1, self.sc70)):
                                count += 1
                        if count == 4:
                            pyautogui.keyDown('SPACE')
                        self.vix = True
                        break


time.sleep(1.5)  # время на переключение с программы на гугл
first_screenshot = pyautogui.screenshot()
length = first_screenshot.size[0]
height = first_screenshot.size[1]
background_colour = first_screenshot.getpixel(((length // 2), (height * 6 // 7)))
if background_colour == (0, 0, 0):
    main_colour = (172, 172, 172)
else:
    main_colour = (83, 83, 83)

base_height = {}

for i in range(15):
    x = length // 3 + length * i // 45
    for y in range(height // 3, height * 5 // 6):
        if first_screenshot.getpixel((x, y)) == main_colour:
            if y in base_height:
                base_height[y] += 1
            else:
                base_height[y] = 1

count = 0

base = -1

for h in base_height:
    if base_height[h] > count:
        count = base_height[h]
        base = h

dino = chrome_dino(base)
print(base)
print(dino.base)
while True:
    dino.vix = False
    dino.screenshot()
    dino.view_area()
    dino.dino_colour()
    dino.find_hurdle()
