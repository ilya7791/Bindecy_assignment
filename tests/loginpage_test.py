from pages.login_page import LoginPage
from pages.main_page import MainPage
from params.parameters import Credentials
from tests.base_test import BaseTest

class TestLogin(BaseTest):
    LOCKED_USER_ERROR = "Epic sadface: Sorry, this user has been locked out."

    def test_login_as_locked_out_user(self):
        login_obj = LoginPage(self.driver)
        login_obj.perform_login(Credentials.LOCKED_OUT_USER, Credentials.PASSWORD)
        error_txt=login_obj.get_login_error()
        mainpage_obj = MainPage(self.driver)
        homepage_header_count=mainpage_obj.get_homepage_header_count()

        # check the right error returned after login as a locked user
        assert error_txt == self.LOCKED_USER_ERROR

        #check locked up user didn't log in
        assert homepage_header_count == 0