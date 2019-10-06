import time

from selenium import webdriver

#Открываем хром
driver = webdriver.Chrome()

#Ждем 5 секунд
time.sleep(5)

#Переходим по ссылке + ждем 5 секунд
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

#Находим элемент на странице
textarea = driver.find_element_by_css_selector(".textarea")

#Вводим текст 'get()' + ждем 5 сек
textarea.send_keys("get()")
time.sleep(5)

#Находим кнопку
submit_button = driver.find_element_by_css_selector(".submit-submission")

#Жмем кнопку + ждем 5 секунд
submit_button.click()
time.sleep(5)

#Закрываем браузер
driver.quit()
