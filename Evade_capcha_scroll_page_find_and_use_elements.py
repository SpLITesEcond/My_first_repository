from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)
    # обьявить функцию для подсчета формулы
    # ln(abs(12*sin(x)))
    # оригинальная формула читабельная для человека


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
    # показать браузеру откуда мы будем брать значение атрибута
find_element_x = browser.find_element_by_id("input_value")
    # внутри лежит id  со значением "х"
    # следующей коммандой мы из атрибута вытянем значение "x"
reset_find_element_x = int(find_element_x.text)
    # значение которое мы вытащили подставиться в функцию
find_regular_expression = calc(reset_find_element_x)
    # пресвоили переменной значение из функции
    # нужно найти поле для подстановки значения
    # втавить значение в поле
fill_field = browser.find_element_by_id("answer")
fill_field.send_keys(find_regular_expression)
    # Проскроллить страницу вниз.
button_Submit = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button_Submit)
    # Выбрать checkbox "I'm the robot".
check_box_true = browser.find_element_by_id("robotCheckbox")
check_box_true.click()
    # Переключить radiobutton "Robots rule!".
select_radiobutton = browser.find_element_by_id("robotsRule")
select_radiobutton.click()
    # Нажать на кнопку "Submit".
button_Submit.click()
time.sleep(4)
browser.quit()
