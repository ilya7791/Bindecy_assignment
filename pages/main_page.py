from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.info_page import InfoPage
from pages.login_page import LoginPage
from params.parameters import SortTypes


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.homepage_header = (By.CSS_SELECTOR, "div.header_label")
        self.add_to_cart_first_item_btn=(By.CSS_SELECTOR, "[class='btn btn_primary btn_small btn_inventory']")
        self.remove_from_cart_first_item_btn = (By.CSS_SELECTOR, "[class='btn btn_secondary btn_small btn_inventory']")
        self.cart_badge=(By.CSS_SELECTOR, "#shopping_cart_container > a")
        self.drop_down=(By.CSS_SELECTOR, "[class='product_sort_container']")
        self.items = (By.CSS_SELECTOR, "[class='inventory_list']>div")
        self.menu_btn = (By.ID, "react-burger-menu-btn")
        self.reset_app_state_btn = (By.ID, "reset_sidebar_link")
        self.logout_link = (By.ID, "logout_sidebar_link")
        self.cart = (By.ID, "shopping_cart_container")

    def sort_items_by_price_low_to_high_and_get_sort_criteria_after_login(self, username, password):
        login_obj = LoginPage(self.driver)
        login_obj.perform_login(username, password)
        self.sort_items(SortTypes.PRICE_LOW_TO_HIGH)
        return self.get_selected_sort()

    def add_first_item_to_cart_after_login_and_get_items_count(self, username, password):
        login_obj = LoginPage(self.driver)
        login_obj.perform_login(username, password)
        self.add_first_item_to_cart()
        return self.get_items_count_in_card_badge()

    def remove_item_from_cart_after_adding_item_to_cart(self, username, password):
        self.add_first_item_to_cart_after_login_and_get_items_count(username, password)
        self.remove_first_item_from_cart()
        return self.get_items_count_in_card_badge()

    def click_cart(self):
        self.click(self.cart)
    def checkout(self, first_name, last_name, set_postal_code):
        self.click_cart()
        cart_obj = CartPage(self.driver)
        cart_obj.click_checkout()
        info_obj = InfoPage(self.driver)
        info_obj.set_info(first_name, last_name, set_postal_code)

    def add_items_starting_with_text_and_get_count(self, prefix):
        items = self.get_items()
        items_found = 0
        for item in items:
            item_name = self.get_item_name(item)
            if prefix in item_name:
                self.add_item_to_cart(item)
                items_found += 1
        return  items_found
    def add_item(self):
        self.add_first_item_to_cart()
    def get_selected_sort(self):
        select = Select(self.get_element(self.drop_down))
        return select.first_selected_option.text
    def click_logout(self):
        self.click(self.logout_link)
    def click_reset_shopping_cart(self):
        self.click(self.reset_app_state_btn)
    def click_menu_btn(self):
        self.click(self.menu_btn)

    def reset_app_state(self):
        self.click_menu_btn()
        self.click_reset_shopping_cart()

    def logout(self):
        self.click_menu_btn()
        self.click_logout()
        login_obj = LoginPage(self.driver)
        return login_obj.get_login_btn_count()

    def add_item_to_cart(self,item):
        btn_text=item.find_element(By.CSS_SELECTOR, "button").text
        if btn_text == "ADD TO CART":
            item.find_element(By.CSS_SELECTOR, "button").click()
    def get_items(self):
        return self.get_elements(self.items)

    def get_item_name(self,item):
        return item.find_element(By.CSS_SELECTOR, "[class='inventory_item_name']").text

    def remove_items_from_cart(self):
        items=self.get_elements(self.items)
        for item in items:
            button_name=item.find_element(By.CSS_SELECTOR, "button").text
            if button_name == "REMOVE":
                item.find_element(By.CSS_SELECTOR, "button").click()

    def select_from_drop_down(self,filter):
        select = Select(self.get_element(self.drop_down))
        select.select_by_visible_text(filter)

    def get_items_count_in_card_badge(self):
        return self.get_text(self.cart_badge)

    def click_cart_badge(self):
        self.click(self.cart_badge)
        return CartPage(self.driver)

    def click_add_to_cart_first_item(self):
        return self.click(self.add_to_cart_first_item_btn)

    def sort_items(self, sort_type):
        self.select_from_drop_down(sort_type)

    def add_first_item_to_cart(self):
        self.click_add_to_cart_first_item()
    def remove_first_item_from_cart(self):
        return self.click(self.remove_from_cart_first_item_btn)
    def get_homepage_header_count(self):
        return len(self.get_elements(self.homepage_header))
