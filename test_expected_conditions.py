from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/explicit_wait2.html')

#Описываем формулу, по которой будем вычислять значение от x
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    #Оговариваем кнопку Book, Submit
    button_book = browser.find_element_by_id('book')
    button_submit = browser.find_element_by_id('solve')


    #Оговариваем строку, в которую нужно ввести ответ на формулу
    answer = browser.find_element_by_id('answer')

    # говорим Selenium проверять в течение 15 секунд, пока цена не упадёт до 100$ + нажимаем кнопку book
    price_100 = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
        )
    button_book.click()

    #Находим X
    x = browser.find_element_by_id('input_value').text

    #Вычисляем значение формулы при x
    y = calc(x)

    #Вводим значение в строку
    answer.send_keys(y)

    #Нажимаем на Submit
    button_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
