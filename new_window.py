from selenium import webdriver
import math
import time

#Считаем по формуле
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    #Открываем браузер
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Нажимаем на кнопку
    button = browser.find_element_by_css_selector('.btn')
    button.click()

    #Переходим на соседнюю вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    #Переходим на страницу и получаем X
    x = browser.find_element_by_css_selector('[id=input_value]')
    x = x.text

    # Считаем переменную
    y = calc(x)

    #Вводим в строку получившееся значение
    input = browser.find_element_by_css_selector('[id=answer]')
    input.send_keys(y)

    #Нажимаем кнопку Submit
    button = browser.find_element_by_css_selector('.btn')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
