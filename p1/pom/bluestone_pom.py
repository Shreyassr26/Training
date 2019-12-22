from p1.base.Action_class import BasePage

class Bluestone_HomePage(BasePage):

    _coins_link_xpath = "//a[@title='Coins']"
    plain_gold_20gram = "//li[@class='active']//span[@class='prcs-d'][contains(text(),'20 gram')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver








