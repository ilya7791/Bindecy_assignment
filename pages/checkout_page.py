from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.title = (By.CSS_SELECTOR, "[class='title']")
        self.items = (By.CSS_SELECTOR, "[class='cart_item']")

    def get_items_count(self):
        return len(self.get_elements(self.items))

    def get_title(self):
        return self.get_text(self.title )
