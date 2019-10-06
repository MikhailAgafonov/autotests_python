from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link_old = "http://suninjuly.github.io/registration1.html"
link_new = "http://suninjuly.github.io/registration2.html"

try:
    # browser = webdriver.Chrome(r'/usr/local/bin/chromedriver/chromedriver)  #line for OS unix
    browser = webdriver.Chrome()  #line for WinOS
    browser.get(link_new)

    input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder~="first"]')
    input1.send_keys("Незнам ")
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder~="last"]')
    input2.send_keys("Незнайкин")
    input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder~="email"]')
    input3.send_keys("neznaika-tester@gmail.com")
    # input4 = browser.find_element(By.CSS_SELECTOR, '[placeholder~="phone"]')
    # input4.send_keys("+7 915 123 45 67")
    # input5 = browser.find_element(By.CSS_SELECTOR, '[placeholder~="address"]')
    # input5.send_keys("Россия, Цветочный город")
    button = browser.find_element(By.XPATH, r'//button[text()="Submit"]')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
