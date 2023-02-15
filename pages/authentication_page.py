"""Authentication Page"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AuthenticationPage(BasePage):
    """Authentication Page class"""

    __INPUT_USERNAME_FIELD = (By.XPATH, '//input[@name="username"]')
    __INPUT_PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')
    __INPUT_SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    __PAGE_MARKER = (By.XPATH, '//h5[text()="Login"]')

    def login_to_app(self, login, password) -> None:
        """User Login"""
        self.fill(by_locator=self.__INPUT_USERNAME_FIELD, value=login)
        self.fill(by_locator=self.__INPUT_PASSWORD_FIELD, value=password)
        self.click(by_locator=self.__INPUT_SUBMIT_BUTTON)

    def check_if_login_page_is_displayed(self) -> bool:
        """Check if page is displayed"""
        return self.is_element_present(by_locator=self.__PAGE_MARKER)
