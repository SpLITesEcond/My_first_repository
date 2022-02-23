import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
auction_by_cell_price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), u"100")
)
button = browser.find_element_by_id("book")
button.click()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
    # показать браузеру откуда мы будем брать значение атрибута
    # выполнить действия на странице
find_element_x = browser.find_element_by_id("input_value")
    # внутри лежит id  со значением "х"
    # следующей коммандой мы из атрибута вытянем значение "x"
reset_find_element_x = int(find_element_x.text)
    # значение которое мы вытащили подставиться в функцию
find_regular_expression = calc(reset_find_element_x)
    # пресвоили переменной значение из функции
fill_field = browser.find_element_by_id("answer")
fill_field.send_keys(find_regular_expression)
    # Нажать на кнопку
press_button = browser.find_element_by_id("solve")
press_button.click()
alert_qiz_answer = browser.switch_to.alert
alert_text = alert_qiz_answer.text
print(alert_text)
