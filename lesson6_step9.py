from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time


def get_browser(headless=False):
    if headless:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(chrome_options=chrome_options)
    else:
        browser = webdriver.Chrome()
    return browser


def fill_form(browser):
    xpath = "//div[@class='first_block']//input[contains(@class, '{}')]"
    browser.find_element_by_xpath(xpath.format("first")).send_keys("first")
    time.sleep(2)
    browser.find_element_by_xpath(xpath.format("second")).send_keys("second")
    time.sleep(2)
    browser.find_element_by_xpath(xpath.format("third")).send_keys("third")
    time.sleep(2)

    return 0


def click_submit(browser):
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    return 0


def wait_for_element(browser, locator, by=By.TAG_NAME, timeout=10):
    WebDriverWait(browser, timeout).until(expected_conditions.visibility_of_element_located((by, locator)))
    time.sleep(5)
    return 0


def main(link, headless=False):
    browser = get_browser(headless)
    try:
        browser.get(link)
        fill_form(browser)
        click_submit(browser)

        wait_for_element(browser, "h1")
        welcome_text = browser.find_element_by_tag_name("h1").text
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        browser.close()
        browser.quit()

    return 0


if __name__ == "__main__":
   main("http://suninjuly.github.io/registration2.html")
