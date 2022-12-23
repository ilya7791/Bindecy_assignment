from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout = (By.ID, "checkout")
        self.remove_btn = (By.ID, "remove-sauce-labs-backpack")
    def click_checkout(self):
        self.click(self.checkout)

    def click_remove_btn(self):
        self.click(self.remove_btn)