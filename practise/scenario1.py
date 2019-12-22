import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def invoke_browser(func):
    def inner(url = "https://www.snapdeal.com/"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(url)
        func(driver)
        driver.close()
    return inner

@invoke_browser
def test_1(driver):
    try:
        driver = webdriver.Chrome()
        driver.find_element_by_id("inputValEnter").send_keys("iphones",Keys.ENTER)
        time.sleep(2)
        iphone = driver.find_element_by_id("131798351").text
        print("Details of iphone are as follows :", iphone)
        print("Test case executed successsfully")
    except Exception as e:
        print(e)
        print("Test case execution failed")

@invoke_browser
def test_2(driver):
    try:
        #driver = webdriver.Chrome()
        driver.find_element_by_xpath("//div[10]//div[4]//div[6]//a[1]").click()
        wh = driver.window_handles
        driver.switch_to.window(wh[1])
        driver.find_element_by_id("add-cart-button-id").click()
        text = driver.find_element_by_xpath("//span[@class='cartQuantity']").text
        print("Total number of items present in cart are :",text)
        print("Test case executeed successfully")
    except Exception as e:
        print(e)
        print("Test cases failed")

@invoke_browser
def test_3(driver):
    try:
        #driver = webdriver.Chrome()
        driver.find_element_by_id("inputValEnter").send_keys("Laptops", Keys.ENTER)
        time.sleep(2)
        sort = driver.find_element_by_xpath("//div[@class='sort-drop clearfix']")
        print(sort.text)
        time.sleep(5)
        sort.click()
        time.sleep(3)
        up_sort=driver.find_element_by_xpath("//div[11]//div[7]//div[1]//div[1]//div[2]//li[5]")
        up_sort.click()
        dis=driver.find_element_by_xpath("//div[@class='sort-drop clearfix']").text
        print(dis)
    except Exception as e:
        print(e)
        print("Test case Failed")

@invoke_browser
def test_4(driver):
    try:
    #driver = webdriver.Chrome()
        user = driver.find_element_by_xpath("//div[@class='accountInner']")
        name = user.text
        action = ActionChains(driver)
        if name == "Sign In":
            action.move_to_element(user)
            driver.find_element_by_xpath("//a[contains(text(),'login')]").click()
            action.perform()
    except Exception as e:
        print(e)
        print()





#test_1()
#test_2()
test_3()
#test_4()