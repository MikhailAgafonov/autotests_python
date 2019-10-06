from selenium import webdriver
import math
import time

#Функция вычисления
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    #Открываем браузер
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Считаем значение от x
    x = browser.find_element_by_id('input_value').text
    y = calc(int(x))

    # Вводим значение X в строку
    x_input = browser.find_element_by_id('answer')
    x_input.send_keys(y)

    # Отмечаем чек-бокс "Я не робот"
    i_am_robot = browser.find_element_by_id('robotCheckbox')
    i_am_robot.click()

    # Отмечаем радио баттон "Я не робот"
    robot_rule = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_rule)
    robot_rule.click()


    # Скроллим до кнопки и отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
