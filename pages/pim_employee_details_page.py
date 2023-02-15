"""Employee Details Page"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PimEmployeeDetailsPage(BasePage):
    """Employee Details Class"""

    # static xpaths
    __PAGE_MARKER = (By.XPATH, '//h6[text() = "Personal Details"]')
    __JOB_MENU_ITEM = (By.XPATH, '//a[text()= "Job"]')
    __JOB_TITLE_DROPDOWN = (By.XPATH, '//label[text()="Job Title"]/..//following-sibling::div//i')
    __JOINED_DATE_DROPDOWN = (By.XPATH, '//input[@placeholder="yyyy-mm-dd"]')
    __TODAY_CALENDAR_BUTTON = (By.XPATH, '//div[text()="Today"]')
    __SAVE_BUTTON = (By.XPATH, '//button[@type="submit"]')

    # dynamic XPaths
    __PAGE_MARKER_NAME = '//h6[text() = "{user_name}"]'
    __JOB_TITLE_LIST_ITEM = '//span[text()="{job_title}" and parent::div[@role="option"]]'

    def check_if_details_page_is_displayed(self) -> bool:
        """Check if Employee Details Page is Displayed"""
        return self.is_element_present(by_locator=self.__PAGE_MARKER)

    def check_if_employee_full_name_is_displayed(self, personal_data: str) -> bool:
        """Check if Employee Details Page is Displayed"""
        person_name_locator = (By.XPATH, self.__PAGE_MARKER_NAME.format(user_name=personal_data))
        return self.is_element_present(by_locator=person_name_locator)

    def click_job_menu_item(self) -> None:
        """Click job menu item"""
        self.click(by_locator=self.__JOB_MENU_ITEM)

    def click_job_title_dropdown(self) -> None:
        """Click Job Title Dropdown"""
        self.click(by_locator=self.__JOB_TITLE_DROPDOWN)

    def click_selected_job_title(self, job_title: str) -> None:
        """click selected job title"""
        job_title_locator = (By.XPATH, self.__JOB_TITLE_LIST_ITEM.format(job_title=job_title))
        self.click(by_locator=job_title_locator)

    def click_joined_date_dropdown(self) -> None:
        """click joined date dropdown"""
        self.click(by_locator=self.__JOINED_DATE_DROPDOWN)

    def click_today_button(self) -> None:
        """click today button"""
        self.click(by_locator=self.__TODAY_CALENDAR_BUTTON)

    def click_save_button(self) -> None:
        """click save button"""
        self.click(by_locator=self.__SAVE_BUTTON)
