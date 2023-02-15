"""Add Employee page"""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PimAddEmployeePage(BasePage):
    """Add Employee class"""
    # static XPaths
    __SAVE_BUTTON = (By.XPATH, '//button[@type="submit"]')

    # dynamic XPaths
    __INPUT_LOCATOR = '//input[@placeholder="{value}"]'

    def fill_input_field(self, field_name: str, field_value: str) -> None:
        """
        Fill [Add Employee] input form
        :param field_name: value of a placeholder of a field to be filled
        :param field_value: new value to by entered
        :return None
        """
        input_field_locator = (By.XPATH, self.__INPUT_LOCATOR.format(value=field_name))
        self.fill(by_locator=input_field_locator, value=field_value)

    def click_save_button(self) -> None:
        """Create a new employee by submitting filled form"""
        self.click(by_locator=self.__SAVE_BUTTON)
