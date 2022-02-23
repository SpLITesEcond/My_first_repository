import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
browser.get(link)
first_num = browser.find_element_by_id("num1")
x = int(first_num.text)
second_num = browser.find_element_by_id("num2")
y = int(second_num.text)
c = int(x + y)
w = str(c)
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(w)  # ищем элемент с текстом "Python"
button = browser.find_element_by_tag_name("button")
time.sleep(1)
button.click()
time.sleep(4)
browser.quit()
