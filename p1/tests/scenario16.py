from selenium import webdriver
from selenium.webdriver import ActionChains


def invoke_browser(func):
    def inner(url):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(url)
        func(driver)
        driver.close()
    return inner






