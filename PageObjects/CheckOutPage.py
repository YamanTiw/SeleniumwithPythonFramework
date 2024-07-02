from selenium.webdriver.common.by import By

from PageObjects.UserInfoPage import UserInfoPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    checkout = (By.CSS_SELECTOR,"button#checkout")
    def clickcheckout(self):
        self.driver.find_element(*CheckOutPage.checkout).click()
        userinfo = UserInfoPage(self.driver)
        return userinfo

