import time

import pytest
from selenium.webdriver.common.by import By


from PageObjects.LoginPage import LoginPage
from PageObjects.ProductPage import ProductPage
from utilities.BaseClass import BaseClass

class TestScriptOne(BaseClass):

    def test_LoginFunctionality(self,getData):

        log = self.getLogger()

        login = LoginPage(self.driver)
        login.enterusername().send_keys(getData["username1"])
        log.info("Username Entered")
        login.enterpassword().send_keys(getData["password1"])
        log.info("Password Entered")


        login.clicklogin()

        Title = login.headervisible()
        assert Title.is_displayed(), "Login Failed"
        print("Login Successful")

    @pytest.fixture(params=[{"username1":"standard_user","password1":"secret_sauce"}])
    def getData(self, request):
        return request.param

    def test_addingProducttoCart(self, getuserData):
        log = self.getLogger()

        productscript = ProductPage(self.driver)
        products = productscript.fetchingproducts()
        for product in products:
            label = productscript.fetchingproductlink()

            if label.text == "Sauce Labs Bike Light":
                productscript.clickaddtocart()
                break

        checkout = productscript.clickcarticon()

        assert self.driver.find_element(By.XPATH, "//a/div").is_displayed(), "Cart button not clickable"


        userinfo = checkout.clickcheckout()

        time.sleep(2)

        userinfo.enterfirstname().send_keys(getuserData["firstname"]) #passing data in key value pairs in the form of dictionary
        userinfo.enterlastname().send_keys(getuserData["lastname"])
        userinfo.enterpincode().send_keys(getuserData["pincode"])
        finishcheckout = userinfo.clickcontinue()

        time.sleep(2)


        finishcheckout.clickfinish()


        assert self.driver.find_element(By.XPATH, "//div/h2").is_displayed(), "Success Message Not Displayed"
        log.info("Order Successful")


    @pytest.fixture(params=[{"firstname":"test", "lastname":"user","pincode":"243001"}])
    def getuserData(self, request):
            return request.param








