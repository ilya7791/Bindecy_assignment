from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
class InfoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.header_label = (By.CSS_SELECTOR, "div.header_label")
        self.first_name=(By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.error_msg = (By.CSS_SELECTOR, "[class='error-message-container error']")

    def open_info_page(self, username, password):
        from pages.main_page import MainPage
        login_page_obj = LoginPage(self.driver)
        login_page_obj.perform_login(username, password)
        mainpage_obj = MainPage(self.driver)
        mainpage_obj.add_first_item_to_cart()
        mainpage_obj.click_cart()
        cart_obj = CartPage(self.driver)
        cart_obj.click_checkout()
    def set_first_name(self, first_name):
        return self.send_text(self.first_name, first_name)

    def set_last_name(self, last_name):
        return self.send_text(self.last_name, last_name)

    def set_postal_code(self, postal_code):
        return self.send_text(self.postal_code, postal_code)

    def click_continue_btn(self):
        return self.click(self.continue_btn)

    def set_info(self, first_name, last_name, set_postal_code):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_postal_code(set_postal_code)
        self.click_continue_btn()

    def get_error_msg(self):
        return self.get_text(self.error_msg)

    def get_header_label(self):
        return self.get_elements(self.header_label)
