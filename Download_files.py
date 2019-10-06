from selenium import webdriver
import time
import os


current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')


try:
    # Открываем браузер
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name_input = browser.find_element_by_css_selector('[name=firstname]')
    first_name_input.send_keys('Mikhail')
    last_name_input = browser.find_element_by_css_selector('[name=lastname]')
    last_name_input.send_keys('Petrov')
    email_name_input = browser.find_element_by_css_selector('[name=email]')
    email_name_input.send_keys('testtest@gmail.com')

    #Грузим файл
    attach_file = browser.find_element_by_css_selector('[type=file]')
    attach_file.send_keys(file_path)
    time.sleep(1)

    #Кликаем submit
    button = browser.find_element_by_css_selector('.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

