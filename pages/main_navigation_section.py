"""Main navigation section"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainNavigationSection(BasePage):
    """Main navigation class"""
    __PIM_BUTTON = (By.XPATH, '//span[text()="PIM"]')

    def click_pim(self) -> None:
        """PIM Click"""
        self.click(by_locator=self.__PIM_BUTTON)
