from selenium import webdriver
import time
from p1.pom.sanpdeal_home import LoginPage

def invoke_browser(func):
    def inner(url):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(url)
        func(driver)
        driver.close()
    return inner

@invoke_browser
def test_1(driver):
    hp = LoginPage(driver)
    hp.login("admin", "manager")

@invoke_browser
def test_2(driver):
    hp = LoginPage(driver)
    hp.login("admin", "manager")
    time.sleep(3)
    hp.click_on_username()

@invoke_browser
def test_3(driver):
    hp = LoginPage(driver)
    hp.login("admin", "manager")
    time.sleep(3)
    hp.click_on_setting_btn()
    time.sleep(1)
    hp.click_on_license_link()



# def test_1(driver):
#     driver.find_element_by_xpath("//button[.='✕']").click()
#     driver.find_element_by_xpath("//input[@placeholder='Search for products, brands and more']").send_keys("iphone",
#                                                                                                            Keys.ENTER)
#     time.sleep(5)
#
# @invoke_browser
# def test_2(driver):
#     time.sleep(3)
#     driver = webdriver.Chrome()
#     driver.find_element_by_xpath("//input[@placeholder='Search for products, brands and more']").send_keys("oneplus", Keys.ENTER)

test_3("http://localhost/login.do")


