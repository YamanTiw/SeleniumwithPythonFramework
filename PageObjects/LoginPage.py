from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.ID,"user-name")
    def enterusername(self):
        return self.driver.find_element(*LoginPage.username)


    password = (By.ID,"password")
    def enterpassword(self):
        return self.driver.find_element(*LoginPage.password)

    loginbutton = (By.ID,"login-button")
    def clicklogin(self):
        return self.driver.find_element(*LoginPage.loginbutton).click()

    Titleheader = (By.CLASS_NAME,"title")
    def headervisible(self):
        return self.driver.find_element(*LoginPage.Titleheader)


