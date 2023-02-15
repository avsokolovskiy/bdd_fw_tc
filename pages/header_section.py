"""Header Section"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HeaderSection(BasePage):
    """Header Section class"""
    __PAGE_NAME = (By.XPATH, '//h6[text()="Dashboard"]')
    __HEADER_PROFILE_PICTURE = (By.XPATH, '//img[@alt="profile picture" and @class="oxd-userdropdown-img"]')
    __LOGOUT_BUTTON = (By.XPATH, '//a[text()="Logout"]')

    def check_if_dashboard_is_displayed(self) -> bool:
        """Check if dashboard is displayed"""
        return self.is_element_present(by_locator=self.__PAGE_NAME)

    def log_out(self) -> None:
        """Check if dashboard is displayed"""
        self.click(by_locator=self.__HEADER_PROFILE_PICTURE)
        self.click(by_locator=self.__LOGOUT_BUTTON)
