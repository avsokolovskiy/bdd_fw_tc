"""PIM Employee list page"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PimEmployeeListPage(BasePage):
    """PIM Employee list page class"""
    __ADD_BUTTON = (By.XPATH, '//button[text()=" Add "]')
    __SEARCH_BUTTON = (By.XPATH, '//button[@type = "submit"]')
    __PENCIL_BUTTON = (By.XPATH, '//i[@class="oxd-icon bi-pencil-fill"]')
    __SEARCH_RESULT_QTY = (By.XPATH, '//span[text() = "(1) Record Found"]')
    __TRASH_BUTTON = (By.XPATH, '//i[@class = "oxd-icon bi-trash"]')
    __DELETE_YES_BUTTON = (By.XPATH, '//button[text() = " Yes, Delete "]')
    __SEARCH_RESULT_EMPTY = (By.XPATH, '//span[text() = "No Records Found"]')
    __SEARCH_RESULTS_TABLE_HEADER_ROW = (By.XPATH, "(//div[@role='row'])[1]")

    # dynamic XPaths
    __SEARCH_INPUT = '//label[text()="{field_name}"]//ancestor::div[contains(@class, "input-field")]//input'
    __TABLE_CELL = '//div[@role="cell"][{cell_index}]'
    __EMPLOYEE_AUTOSUGGEST_LIST_ELEMENT = '//div[@role="listbox"]//span[normalize-space()="{user_name}"]'

    def click_add_button(self) -> None:
        """click add button"""
        self.click(by_locator=self.__ADD_BUTTON)

    def fill_search_form(self, field_name: str, field_value: str) -> None:
        """input search string"""
        input_field_locator = (By.XPATH, self.__SEARCH_INPUT.format(field_name=field_name))
        self.fill(by_locator=input_field_locator, value=field_value)

    def click_search_button(self) -> None:
        """click search button"""
        self.click(by_locator=self.__SEARCH_BUTTON)

    def get_cell_text(self, column_name: str) -> str:
        """get PIM table cell text"""
        table_headers = self.get_element_text(by_locator=self.__SEARCH_RESULTS_TABLE_HEADER_ROW).split("\n")
        cell_index = table_headers.index(column_name)
        # +2 -> +1 because of skipped check field, +1 because of indexing from 0 in lists
        expected_column_locator = (By.XPATH, self.__TABLE_CELL.format(cell_index=cell_index+2))
        return self.get_element_text(by_locator=expected_column_locator)

    def click_pencil_button(self) -> None:
        """click pencil button"""
        self.click(by_locator=self.__PENCIL_BUTTON)

    def click_employee_autosuggest_list_element(self, test_user_name) -> None:
        """click employee auto-suggest list_element"""
        self.click(by_locator=(By.XPATH, self.__EMPLOYEE_AUTOSUGGEST_LIST_ELEMENT.format(user_name=test_user_name)))

    def check_if_search_results_qty_1(self) -> bool:
        """get_search_results_qty"""
        return self.is_element_present(by_locator=self.__SEARCH_RESULT_QTY)

    def click_trash_button(self) -> None:
        """click trash button"""
        self.click(by_locator=self.__TRASH_BUTTON)

    def click_delete_yes_button(self) -> None:
        """click delete yes button"""
        self.click(by_locator=self.__DELETE_YES_BUTTON)

    def check_if_search_results_empty(self) -> bool:
        """check if search results empty"""
        return self.is_element_present(by_locator=self.__SEARCH_RESULT_EMPTY)
