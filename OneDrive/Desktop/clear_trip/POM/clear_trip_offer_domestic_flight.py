
from selenium import webdriver
import time
from data import reading_objects
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

login_obj = reading_objects.read_locators()
print(login_obj)

class Offerpage:
    def __init__(self,driver_1):
        self.driver_1 = driver_1

    def click_login(self):
        self.driver_1.find_element(*login_obj["click_login_popup"]).click()
        time.sleep(1)

    def click_offers(self):
        self.driver_1.parent_window = self.driver_1.current_window_handle
        self.driver_1.find_element(*login_obj["click_Offers"]).click()
        time.sleep(2)

    def window_alter(self):
        child_window = self.driver_1.window_handles
        print("parent window handle name is", self.driver_1.parent_window)
        print("type of windows", type(child_window))

        for child in child_window:
            print(child)
            if self.driver_1.parent_window != child:
                print("Switching to new window/tab")
                self.driver_1.switch_to.window(child)
                print("title is", self.driver_1.title)
        time.sleep(5)

    def click_domestic_flight(self):
        self.driver_1.find_element(*login_obj["click_domestic_flight"]).click()
        time.sleep(2)

    def click_one_offer(self):
        self.driver_1.find_element(*login_obj["click_one_offer"]).click()
        time.sleep(1)
        ActionChains(self.driver_1).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)

    def click_white_space(self):
        self.driver_1.find_element(*login_obj["click_white_space"]).click()
        time.sleep(2)
        ActionChains(self.driver_1).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)

    def click_book_button(self):
        self.driver_1.find_element(*login_obj["click_book_button"]).click()
        time.sleep(3)



