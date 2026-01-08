import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class PersonalPage(BasePage):
    PAGE_URL = Links.PERSONAL_PAGE
    FIRST_NAME_FIELD = (By.XPATH, "//input[@name='firstName']")
    SAVE_BUTTON = (By.XPATH, "(//button[@type='button'])[1]")
    SPINNER = (By.XPATH, "//div[@class='oxd-loading-spinner']")

    def change_name(self, new_name):
        with allure.step(f"Change name on '{new_name}'"):
            first_name_field = self.wait.until(
                EC.element_to_be_clickable(self.FIRST_NAME_FIELD)
            )
            # Надежный способ очистить поле:
            first_name_field.clear()

            # Проверка сразу после очистки, без sleep:
            assert first_name_field.get_attribute("value") == "", "There is text"

            first_name_field.send_keys(new_name)
            self.new_name = new_name

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Changes have been saved successfully")
    def is_changes_saved(self):
        # self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
        # self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        self.wait.until(
            EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.new_name)
        )
