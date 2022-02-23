from selenium import webdriver
import time
    # from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/math.html"
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
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
