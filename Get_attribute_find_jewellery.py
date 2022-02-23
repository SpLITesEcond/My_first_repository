from selenium import webdriver
# from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex")
y = calc(x)
    # Найти эллемент в котором зашифровано значение
enter_your_answer_in_form = browser.find_element_by_id("answer")
enter_your_answer_in_form.send_keys(y)
    # Отметить checkbox "I'm the robot".
check_box_true = browser.find_element_by_id("robotCheckbox")
check_box_true.click()
    # Выбрать radiobutton "Robots rule!".
select_radiobutton = browser.find_element_by_id("robotsRule")
select_radiobutton.click()
time.sleep(4)
    # Нажать на кнопку Submit.
button_Submit = browser.find_element_by_tag_name("button")
button_Submit.click()
time.sleep(6)
browser.quit()
