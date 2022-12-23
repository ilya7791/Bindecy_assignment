from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.user_name_box = (By.ID, "user-name")
        self.password_box = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")
        self.login_error = (By.CSS_SELECTOR, "div.error-message-container.error")

    def login(self, user_type, password):
        self.perform_login(user_type, password)
    def get_login_btn_count(self):
        return len(self.get_elements(self.login_btn))
    def get_login_error(self):
        return self.get_text(self.login_error)
    def click_login_btn(self):
        self.click(self.login_btn)

    def insert_user_name(self, user_name):
        self.send_text(self.user_name_box, user_name)
    def insert_user_password(self, user_password):
        self.send_text(self.password_box,user_password)

    def perform_login(self, user_name, user_password):
        self.insert_user_name(user_name)
        self.insert_user_password(user_password)
        self.click_login_btn()

