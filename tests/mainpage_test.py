from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from params.parameters import Credentials, SortTypes
from tests.base_test import BaseTest
class TestMainPage(BaseTest):
    EXPECTED_PREFIX_TEXT = "Sauce Labs"
    EXPECTED_CHECKOUT_PAGE_TITLE = "CHECKOUT: OVERVIEW"

    def test_add_item_from_main_page_standard_user(self):
        mainpage_obj = MainPage(self.driver)
        items_in_badge_count = mainpage_obj.add_first_item_to_cart_after_login_and_get_items_count(
            Credentials.STANDARD_USER, Credentials.PASSWORD)
        assert items_in_badge_count == "1", f"Expected 1 item, but got {items_in_badge_count}"

    def test_add_item_from_main_page_performance_glitch_user(self):
        mainpage_obj = MainPage(self.driver)
        items_in_badge_count = mainpage_obj.add_first_item_to_cart_after_login_and_get_items_count(
            Credentials.PERFORMANCE_GLITCH_USER, Credentials.PASSWORD)
        assert items_in_badge_count == "1", f"Expected 1 item, but got {items_in_badge_count}"

    def test_add_item_from_main_page_problem_user(self):
        mainpage_obj = MainPage(self.driver)
        items_in_badge_count = mainpage_obj.add_first_item_to_cart_after_login_and_get_items_count(
            Credentials.PROBLEM_USER, Credentials.PASSWORD)
        assert items_in_badge_count == "1", f"Expected 1 item, but got {items_in_badge_count}"

    def test_remove_item_standard_user(self):
        mainpage_obj = MainPage(self.driver)
        items_in_badge_count = mainpage_obj.remove_item_from_cart_after_adding_item_to_cart(Credentials.STANDARD_USER,
                                                                                            Credentials.PASSWORD)
        assert items_in_badge_count == "", f"Expected empty cart, but got {items_in_badge_count}"

    def test_remove_item_performance_glitch_user(self):
        mainpage_obj = MainPage(self.driver)
        items_in_badge_count = mainpage_obj.remove_item_from_cart_after_adding_item_to_cart(
            Credentials.PERFORMANCE_GLITCH_USER,
            Credentials.PASSWORD)
        assert items_in_badge_count == "", f"Expected empty cart, but got {items_in_badge_count}"

    def test_remove_item_problem_user(self):
        mainpage_obj = MainPage(self.driver)
        items_in_badge_count = mainpage_obj.remove_item_from_cart_after_adding_item_to_cart(Credentials.PROBLEM_USER,
                                                                                            Credentials.PASSWORD)
        assert items_in_badge_count == "", f"Expected empty cart, but got {items_in_badge_count}"

    def test_add_cheepest_and_most_expensive_item_to_cart_standard_user(self):
        mainpage_obj = MainPage(self.driver)
        actual_sort_type = mainpage_obj.sort_items_by_price_low_to_high_and_get_sort_criteria_after_login(
            Credentials.STANDARD_USER, Credentials.PASSWORD)
        assert actual_sort_type == SortTypes.PRICE_LOW_TO_HIGH, f"Expected {SortTypes.PRICE_LOW_TO_HIGH} ," \
                                                                f" but got {actual_sort_type}"
        mainpage_obj.add_first_item_to_cart()
        items_in_badge_count = mainpage_obj.get_items_count_in_card_badge()
        assert items_in_badge_count == "1", f"Expected 1 item, but got {items_in_badge_count}"
        mainpage_obj.sort_items(SortTypes.PRICE_HIGH_TO_LOW)
        actual_sort_type = mainpage_obj.get_selected_sort()
        assert actual_sort_type == SortTypes.PRICE_HIGH_TO_LOW, f"Expected {SortTypes.PRICE_HIGH_TO_LOW} ," \
                                                                f" but got {actual_sort_type}"

        mainpage_obj.add_first_item_to_cart()
        items_in_badge_count = mainpage_obj.get_items_count_in_card_badge()
        assert items_in_badge_count == "2", f"Expected 2 item, but got {items_in_badge_count}"

    def test_add_cheepest_and_most_expensive_item_to_cart_performance_glitch_user(self):
        mainpage_obj = MainPage(self.driver)
        actual_sort_type = mainpage_obj.sort_items_by_price_low_to_high_and_get_sort_criteria_after_login(
            Credentials.PERFORMANCE_GLITCH_USER, Credentials.PASSWORD)
        assert actual_sort_type == SortTypes.PRICE_LOW_TO_HIGH, f"Expected {SortTypes.PRICE_LOW_TO_HIGH} ," \
                                                                f" but got {actual_sort_type}"
        mainpage_obj.add_first_item_to_cart()
        items_in_badge_count = mainpage_obj.get_items_count_in_card_badge()
        assert items_in_badge_count == "1", f"Expected 1 item, but got {items_in_badge_count}"
        mainpage_obj.sort_items(SortTypes.PRICE_HIGH_TO_LOW)
        actual_sort_type = mainpage_obj.get_selected_sort()
        assert actual_sort_type == SortTypes.PRICE_HIGH_TO_LOW, f"Expected {SortTypes.PRICE_HIGH_TO_LOW} ," \
                                                                f" but got {actual_sort_type}"

        mainpage_obj.add_first_item_to_cart()
        items_in_badge_count = mainpage_obj.get_items_count_in_card_badge()
        assert items_in_badge_count == "2", f"Expected 2 item, but got {items_in_badge_count}"

    def test_add_cheepest_and_most_expensive_item_to_cart_problem_user(self):
        mainpage_obj = MainPage(self.driver)
        actual_sort_type = mainpage_obj.sort_items_by_price_low_to_high_and_get_sort_criteria_after_login(
            Credentials.PROBLEM_USER, Credentials.PASSWORD)
        assert actual_sort_type == SortTypes.PRICE_LOW_TO_HIGH, f"Expected {SortTypes.PRICE_LOW_TO_HIGH} ," \
                                                                f" but got {actual_sort_type}"
        mainpage_obj.add_first_item_to_cart()
        items_in_badge_count = mainpage_obj.get_items_count_in_card_badge()
        assert items_in_badge_count == "1", f"Expected 1 item, but got {items_in_badge_count}"
        mainpage_obj.sort_items(SortTypes.PRICE_HIGH_TO_LOW)
        actual_sort_type = mainpage_obj.get_selected_sort()
        assert actual_sort_type == SortTypes.PRICE_HIGH_TO_LOW, f"Expected {SortTypes.PRICE_HIGH_TO_LOW} ," \
                                                                f" but got {actual_sort_type}"

        mainpage_obj.add_first_item_to_cart()
        items_in_badge_count = mainpage_obj.get_items_count_in_card_badge()
        assert items_in_badge_count == "2", f"Expected 2 item, but got {items_in_badge_count}"

    def test_add_items_that_start_with_word_sauce_Labs_to_cart_standard_user(self):
        login_obj = LoginPage(self.driver)
        login_obj.perform_login(Credentials.STANDARD_USER, Credentials.PASSWORD)
        mainpage_obj = MainPage(self.driver)
        items_found = mainpage_obj.add_items_starting_with_text_and_get_count(prefix=self.EXPECTED_PREFIX_TEXT)
        items_in_badge_count = mainpage_obj.get_items_count_in_card_badge()
        assert int(items_in_badge_count) == items_found, f"Expected {items_found}," \
                                                         f" but got {items_in_badge_count}"

    def test_add_items_that_start_with_word_sauce_Labs_to_cart_performance_glitch_user(self):
        login_obj = LoginPage(self.driver)
        login_obj.perform_login(Credentials.STANDARD_USER, Credentials.PASSWORD)
        mainpage_obj = MainPage(self.driver)
        items_found = mainpage_obj.add_items_starting_with_text_and_get_count(prefix=self.EXPECTED_PREFIX_TEXT)
        items_in_badge_count = mainpage_obj.get_items_count_in_card_badge()
        assert int(items_in_badge_count) == items_found, f"Expected {items_found}," \
                                                         f" but got {items_in_badge_count}"

    def test_add_items_that_start_with_word_sauce_Labs_to_cart_problem_user(self):
        login_obj = LoginPage(self.driver)
        login_obj.perform_login(Credentials.STANDARD_USER, Credentials.PASSWORD)
        mainpage_obj = MainPage(self.driver)
        items_found = mainpage_obj.add_items_starting_with_text_and_get_count(prefix=self.EXPECTED_PREFIX_TEXT)
        items_in_badge_count = mainpage_obj.get_items_count_in_card_badge()
        assert int(items_in_badge_count) == items_found, f"Expected {items_found}," \
                                                         f" but got {items_in_badge_count}"

    def test_purchase_item_standard_user(self):
        mainpage_obj = MainPage(self.driver)
        items_in_badge_count = mainpage_obj.add_first_item_to_cart_after_login_and_get_items_count(
            Credentials.STANDARD_USER, Credentials.PASSWORD)
        assert items_in_badge_count == "1", f"Expected 1 item, but got {items_in_badge_count}"
        mainpage_obj = MainPage(self.driver)
        mainpage_obj.checkout(first_name="aaa", last_name="bbb", set_postal_code="123")
        checkout_obj = CheckoutPage(self.driver)
        title = checkout_obj.get_title()
        assert title == self.EXPECTED_CHECKOUT_PAGE_TITLE, "Not in checkout page"
        checkout_obj = CheckoutPage(self.driver)
        items_in_checkout_count = checkout_obj.get_items_count()
        assert items_in_checkout_count == int(items_in_badge_count)

    def test_purchase_item_performance_glitch_user(self):
        mainpage_obj = MainPage(self.driver)
        items_in_badge_count = mainpage_obj.add_first_item_to_cart_after_login_and_get_items_count(
            Credentials.PERFORMANCE_GLITCH_USER, Credentials.PASSWORD)
        assert items_in_badge_count == "1", f"Expected 1 item, but got {items_in_badge_count}"
        mainpage_obj = MainPage(self.driver)
        mainpage_obj.checkout(first_name="aaa", last_name="bbb", set_postal_code="123")
        checkout_obj = CheckoutPage(self.driver)
        title = checkout_obj.get_title()
        assert title == "CHECKOUT: OVERVIEW", "Not in checkout page"
        checkout_obj = CheckoutPage(self.driver)
        items_in_checkout_count = checkout_obj.get_items_count()
        assert items_in_checkout_count == int(items_in_badge_count)

    def test_purchase_item_problem_user(self):
        mainpage_obj = MainPage(self.driver)
        items_in_badge_count = mainpage_obj.add_first_item_to_cart_after_login_and_get_items_count(
            Credentials.PROBLEM_USER, Credentials.PASSWORD)
        assert items_in_badge_count == "1", f"Expected 1 item, but got {items_in_badge_count}"
        mainpage_obj = MainPage(self.driver)
        mainpage_obj.checkout(first_name="aaa", last_name="bbb", set_postal_code="123")
        checkout_obj = CheckoutPage(self.driver)
        title = checkout_obj.get_title()
        assert title == "CHECKOUT: OVERVIEW", "Not in checkout page"
        checkout_obj = CheckoutPage(self.driver)
        items_in_checkout_count = checkout_obj.get_items_count()
        assert items_in_checkout_count == int(items_in_badge_count)

    def test_reset_app_state_standard_user(self):
        mainpage_obj = MainPage(self.driver)
        items_in_badge_count = mainpage_obj.add_first_item_to_cart_after_login_and_get_items_count(
            Credentials.STANDARD_USER, Credentials.PASSWORD)
        assert items_in_badge_count == "1", f"Expected 1 item, but got {items_in_badge_count}"
        mainpage_obj = MainPage(self.driver)
        mainpage_obj.reset_app_state()
        items_in_badge_count = mainpage_obj.get_items_count_in_card_badge()
        assert items_in_badge_count == "", f"Expected empty cart, but got {items_in_badge_count}"

    def test_reset_app_state_performance_glitch_user(self):
        mainpage_obj = MainPage(self.driver)
        items_in_badge_count = mainpage_obj.add_first_item_to_cart_after_login_and_get_items_count(
            Credentials.PERFORMANCE_GLITCH_USER, Credentials.PASSWORD)
        assert items_in_badge_count == "1", f"Expected 1 item, but got {items_in_badge_count}"
        mainpage_obj = MainPage(self.driver)
        mainpage_obj.reset_app_state()
        items_in_badge_count = mainpage_obj.get_items_count_in_card_badge()
        assert items_in_badge_count == "", f"Expected empty cart, but got {items_in_badge_count}"

    def test_reset_app_state_problem_user(self):
        mainpage_obj = MainPage(self.driver)
        items_in_badge_count = mainpage_obj.add_first_item_to_cart_after_login_and_get_items_count(
            Credentials.PROBLEM_USER, Credentials.PASSWORD)
        assert items_in_badge_count == "1", f"Expected 1 item, but got {items_in_badge_count}"
        mainpage_obj = MainPage(self.driver)
        mainpage_obj.reset_app_state()
        items_in_badge_count = mainpage_obj.get_items_count_in_card_badge()
        assert items_in_badge_count == "", f"Expected empty cart, but got {items_in_badge_count}"

    def test_logout_standard_user(self):
        login_obj = LoginPage(self.driver)
        login_obj.perform_login(Credentials.STANDARD_USER, Credentials.PASSWORD)
        mainpage_obj = MainPage(self.driver)
        logout_btn_count = mainpage_obj.logout()
        assert logout_btn_count == 1, "not in logout page"

    def test_logout_performance_glitch_user(self):
        login_obj = LoginPage(self.driver)
        login_obj.perform_login(Credentials.PERFORMANCE_GLITCH_USER, Credentials.PASSWORD)
        mainpage_obj = MainPage(self.driver)
        logout_btn_count = mainpage_obj.logout()
        assert logout_btn_count == 1, "not in logout page"

    def test_logout_problem_user(self):
        login_obj = LoginPage(self.driver)
        login_obj.perform_login(Credentials.PROBLEM_USER, Credentials.PASSWORD)
        mainpage_obj = MainPage(self.driver)
        logout_btn_count = mainpage_obj.logout()
        assert logout_btn_count == 1, "not in logout page"
