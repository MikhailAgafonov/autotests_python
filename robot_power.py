from selenium import webdriver
import math
import time

# Считаем переменную
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    #Считаем, чему равен x
    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    # Вводим значение X в строку
    x_input = browser.find_element_by_id('answer')
    x_input.send_keys(y)

    # Отмечаем чек-бокс "Я не робот"
    i_am_robot = browser.find_element_by_id('robotCheckbox')
    i_am_robot.click()

    # Отмечаем чек-бокс "Я не робот"
    robot_rule = browser.find_element_by_id('robotsRule')
    robot_rule.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
