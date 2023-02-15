"""Base page"""
from behave.runner import Context
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

DRIVER_SERVICE = Service(executable_path=ChromeDriverManager().install())
DRIVER_WAIT_TIME = 8


class BasePage:
    """Base page class"""
    driver = None

    def __init__(self, context: Context):
        self.driver = context.driver
        self.explicitly_wait = WebDriverWait(driver=self.driver, timeout=DRIVER_WAIT_TIME)

    def go_to_url(self, url):
        """go to URL method"""
        self.driver.get(url)

    def get_element(self, by_locator) -> WebElement:
        return self.explicitly_wait.until(expected_conditions.visibility_of_element_located(by_locator),
                                          message=f'{by_locator} is not found on the page')

    def is_element_present(self, by_locator) -> bool:
        """Get WD element"""
        element_is_present = True
        try:
            self.get_element(by_locator=by_locator)
        except TimeoutException:
            element_is_present = False
        return element_is_present

    def get_element_text(self, by_locator) -> str:
        """Get element text"""
        return self.get_element(by_locator=by_locator).text

    def click(self, by_locator) -> None:
        """Click on element"""
        self.get_element(by_locator=by_locator).click()

    def fill(self, by_locator, value) -> None:
        """Fill intput box"""
        self.get_element(by_locator=by_locator).send_keys(value)

    def quite_driver(self) -> None:
        """Quit WD"""
        self.driver.quit()
