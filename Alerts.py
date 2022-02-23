from selenium import webdriver
import time
import math
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
    # показать браузеру откуда мы будем брать значение атрибута
browser.get(link)
    # Нажать на кнопку
press_button = browser.find_element_by_tag_name("button")
press_button.click()
    # Принять confirm
confirm_alert = browser.switch_to_alert()
confirm_alert.accept()
    #выполнить действия на странице
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
button_Submit = browser.find_element_by_tag_name("button")
button_Submit.click()
    #получить значиние из алерта
alert_qiz_answer = browser.switch_to.alert
alert_text = alert_qiz_answer.text
print(alert_text)
time.sleep(5)
browser.quit()

