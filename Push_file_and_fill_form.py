import os
from selenium import webdriver
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
try:
    #Заполнить текстовые поля: имя, фамилия, email
    fill_fild_name = browser.find_element_by_name("firstname")
    fill_fild_name.send_keys("Roman")
    fill_fild_last_name = browser.find_element_by_name("lastname")
    fill_fild_last_name.send_keys("LRoman")
    fill_fild_email = browser.find_element_by_name("email")
    fill_fild_email.send_keys("LRoman@mail.wa")
    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    send = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'Checkbox_radiobutton_Что_я_узнал.txt')
    send.send_keys(file_path)
    # Нажать кнопку "Submit"
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()
finally:
    time.sleep(6)
    browser.quit()
