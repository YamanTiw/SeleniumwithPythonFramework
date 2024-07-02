from selenium.webdriver.common.by import By

from PageObjects.FinalCheckOutPage import FinalCheckOutPage


class UserInfoPage:
    def __init__(self, driver):
        self.driver = driver

    firstname = (By.ID,"first-name")
    def enterfirstname(self):
        return self.driver.find_element(*UserInfoPage.firstname)

    lastname = (By.ID, "last-name")

    def enterlastname(self):
        return self.driver.find_element(*UserInfoPage.lastname)

    pincode = (By.ID, "postal-code")

    def enterpincode(self):
        return self.driver.find_element(*UserInfoPage.pincode)

    continuebutton = (By.ID, "continue")

    def clickcontinue(self):
        self.driver.find_element(*UserInfoPage.continuebutton).click()
        finishcheckout = FinalCheckOutPage(self.driver)
        return finishcheckout


