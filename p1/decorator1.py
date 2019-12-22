def invoke_browser(func):
    def inner(url):
        print("druver=webdriver.Chrome()")
        print("driver.get({})".format(url))
        func("driver")
        print("driver.close()")
    return inner
@invoke_browser
def test_1(driver):
    print("test case 1 is running using", driver)
@invoke_browser
def test_2(driver):
    print("test case 2 is running using", driver)

test_1("facebook")
print("--------------------------------")
test_2("twitter")