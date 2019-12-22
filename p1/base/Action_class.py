from selenium.webdriver.common.by import By
import logging
class BasePage():

    def __init__(self, driver):
        # super(BasePage, self).__init__(driver)
        self.driver = driver


    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            pass
            # self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            #self.log.info("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            pass
           # self.log.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            #self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            pass
            #self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            #self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            pass
            #self.log.info("Cannot send data on the element with locator: " + locator +
                         # " locatorType: " + locatorType)
