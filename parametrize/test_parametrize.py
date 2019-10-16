import pytest
import time
import math
from selenium import webdriver

answer = math.log(int(time.time()))

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture
def logging_fails():
    print(Correct)

@pytest.mark.parametrize('params', ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
                                    'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
                                    'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
                                    'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1'])
def test_guest_should_see_login_link(browser, params):

    #Присваиваем адрес ссылке
    link = params
    browser.get(link)
    browser.implicitly_wait(15)

    #Находим поле, вводим значение
    input = browser.find_element_by_css_selector('.textarea')
    answer = math.log(int(time.time()))
    answer = str(answer)
    input.send_keys(answer)

    #Тыкаем на кнопку
    browser.implicitly_wait(15)
    button = browser.find_element_by_css_selector('.submit-submission')
    button.click()

    #Ожидаем загрузки надписи Correct!
    browser.implicitly_wait(15)
    Correct = browser.find_element_by_css_selector('.smart-hints__hint')
    assert Correct.text == 'Correct!', 'It is not "Correct!"'

