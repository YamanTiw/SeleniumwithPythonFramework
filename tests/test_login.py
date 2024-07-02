import time

import pytest
from selenium.webdriver.common.by import By

from PageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass

class TestScriptOne(BaseClass):

    def test_LoginFunctionality(self, getData):

        login = LoginPage(self.driver)
        login.enterusername().send_keys(getData[0])
        login.enterpassword().send_keys(getData[1])
        login.clicklogin()

        Title = login.headervisible()
        assert Title.is_displayed(), "Login Failed"
        print("Login Successful")



    @pytest.fixture(params=[("standard_user","secret_sauce")])
    def getData(self, request):
        return request.param

