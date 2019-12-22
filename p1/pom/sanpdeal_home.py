from p1.base.Action_class import BasePage

class LoginPage(BasePage):
    #locators

    _email_field_id = "username"
    _password_field_name = "pwd"
    _login_button_xpath = "//a[@id='loginButton']//div[contains(text(),'Login')]"
    _username = "//a[@class='userProfileLink username']"
    _setting_button_xpath = "//div[@class='popup_menu_icon warning_icon']"
    _license_btn = "//a[contains(text(),'Licenses')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field_id)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field_name, "name")

    def clickLoginButton(self):
        self.elementClick(self._login_button_xpath, "xpath")

    def login(self, email="", password=""):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def click_on_username(self):
        self.elementClick(self._username,"xpath")

    def click_on_setting_btn(self):
        self.elementClick(self._setting_button_xpath, "xpath")

    def click_on_license_link(self):
        self.elementClick(self._license_btn,"xpath")