from selenium.webdriver.common.by import By


class FinalCheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    finish = (By.ID,"finish")
    def clickfinish(self):
        return self.driver.find_element(*FinalCheckOutPage.finish).click()

