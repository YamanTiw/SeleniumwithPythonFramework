from selenium.webdriver.common.by import By

from PageObjects.CheckOutPage import CheckOutPage


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    product = (By.XPATH,"//a/div")
    def fetchingproducts(self):
        return self.driver.find_elements(*ProductPage.product)

    productlink = (By.LINK_TEXT, "Sauce Labs Bike Light")

    def fetchingproductlink(self):
        return self.driver.find_element(*ProductPage.productlink)

    addtocart = (By.NAME, "add-to-cart-sauce-labs-backpack")

    def clickaddtocart(self):
        return self.driver.find_element(*ProductPage.addtocart).click()

    carticon = (By.CLASS_NAME,"shopping_cart_link")
    def clickcarticon(self):
        self.driver.find_element(*ProductPage.carticon).click()
        checkout = CheckOutPage(self.driver)
        return checkout




