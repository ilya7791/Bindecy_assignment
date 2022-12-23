from pages.checkout_page import CheckoutPage
from pages.info_page import InfoPage
from params.parameters import Credentials
from tests.base_test import BaseTest

class TestInfoPage(BaseTest):

    def test_info_standard_user(self):
        info_obj = InfoPage(self.driver)
        info_obj.open_info_page(Credentials.STANDARD_USER, Credentials.PASSWORD)

        # empty inputs
        info_obj.set_info(first_name="", last_name="", set_postal_code="")
        error_msg=info_obj.get_error_msg()
        assert error_msg == "Error: First Name is required", f"Expected: First Name is required, but got {error_msg}"

        # empty last name
        info_obj.set_info(first_name="aaa", last_name="", set_postal_code="") # empty inputs
        error_msg=info_obj.get_error_msg()
        assert error_msg == "Error: Last Name is required", f"Expected: Last Name is required, but got {error_msg}"

        # empty post code
        info_obj.set_info(first_name="aaa", last_name="bbb", set_postal_code="")
        error_msg=info_obj.get_error_msg()
        assert error_msg == "Error: Postal Code is required", f"Expected: Error: Postal Code is required, but got {error_msg}"

        # positive test: all inputs are correct
        info_obj.set_info(first_name="aaa", last_name="bbb", set_postal_code="123")
        checkout_obj = CheckoutPage(self.driver)
        title=checkout_obj.get_title()
        assert title == "CHECKOUT: OVERVIEW"

    def test_info_performance_glitch_user(self):
        info_obj = InfoPage(self.driver)
        info_obj.open_info_page(Credentials.PERFORMANCE_GLITCH_USER, Credentials.PASSWORD)

        # empty inputs
        info_obj.set_info(first_name="", last_name="", set_postal_code="")
        error_msg=info_obj.get_error_msg()
        assert error_msg == "Error: First Name is required", f"Expected: First Name is required, but got {error_msg}"

        # empty last name
        info_obj.set_info(first_name="aaa", last_name="", set_postal_code="") # empty inputs
        error_msg=info_obj.get_error_msg()
        assert error_msg == "Error: Last Name is required", f"Expected: Last Name is required, but got {error_msg}"

        # empty post code
        info_obj.set_info(first_name="aaa", last_name="bbb", set_postal_code="")
        error_msg=info_obj.get_error_msg()
        assert error_msg == "Error: Postal Code is required", f"Expected: Error: Postal Code is required, but got {error_msg}"

        # positive test: all inputs are correct
        info_obj.set_info(first_name="aaa", last_name="bbb", set_postal_code="123")
        checkout_obj = CheckoutPage(self.driver)
        title=checkout_obj.get_title()
        assert title == "CHECKOUT: OVERVIEW"

    def test_info_problem_user(self):
        info_obj = InfoPage(self.driver)
        info_obj.open_info_page(Credentials.PROBLEM_USER, Credentials.PASSWORD)

        # empty inputs
        info_obj.set_info(first_name="", last_name="", set_postal_code="")
        error_msg=info_obj.get_error_msg()
        assert error_msg == "Error: First Name is required", f"Expected: First Name is required, but got {error_msg}"

        # empty last name
        info_obj.set_info(first_name="aaa", last_name="", set_postal_code="") # empty inputs
        error_msg=info_obj.get_error_msg()
        assert error_msg == "Error: Last Name is required", f"Expected: Last Name is required, but got {error_msg}"

        # empty post code
        info_obj.set_info(first_name="aaa", last_name="bbb", set_postal_code="")
        error_msg=info_obj.get_error_msg()
        assert error_msg == "Error: Postal Code is required", f"Expected: Error: Postal Code is required, but got {error_msg}"

        # positive test: all inputs are correct
        info_obj.set_info(first_name="aaa", last_name="bbb", set_postal_code="123")
        checkout_obj = CheckoutPage(self.driver)
        title=checkout_obj.get_title()
        assert title == "CHECKOUT: OVERVIEW"