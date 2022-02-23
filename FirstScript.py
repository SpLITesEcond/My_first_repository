from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element_by_tag_name("[name=\"first_name\"]")
input1.send_keys("Ivan")
input2 = browser.find_element_by_tag_name("[name=\"last_name\"]")
input2.send_keys("Petrov")
input3 = browser.find_element_by_tag_name("[name=\"firstname\"]")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()
    # успеваем скопировать код за 30 секунд
time.sleep(15)
    # Выход из драйвера
browser.quit()

