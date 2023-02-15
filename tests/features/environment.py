from allure import attach, attachment_type
from behave.runner import Context
from hamcrest import assert_that

from pages.authentication_page import AuthenticationPage
from pages.header_section import HeaderSection
from pages.main_navigation_section import MainNavigationSection
from pages.pim_add_employee_page import PimAddEmployeePage
from pages.pim_employee_details_page import PimEmployeeDetailsPage
from pages.pim_employee_list_page import PimEmployeeListPage
from utils.capabilities_util import get_driver

URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
ADMIN_PASSWORD = 'admin123'
ADMIN_LOGIN = 'Admin'


def before_all(context: Context):
    setup = context.config.userdata
    context.driver = get_driver(browser=setup["browser"], resolution_h=int(setup["resolution_h"]),
                                resolution_w=int(setup["resolution_w"]))
    context.header_section = HeaderSection(context=context)
    context.authentication_page = AuthenticationPage(context=context)
    context.main_navigation_section = MainNavigationSection(context=context)
    context.pim_employee_list_page = PimEmployeeListPage(context=context)
    context.pim_add_employee_page = PimAddEmployeePage(context=context)
    context.pim_employee_details_page = PimEmployeeDetailsPage(context=context)
    context.authentication_page.go_to_url(url=URL)
    context.authentication_page.login_to_app(login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
    dashboard_is_displayed = context.header_section.check_if_dashboard_is_displayed()
    assert_that(dashboard_is_displayed)


def after_scenario(context: Context, scenario):
    if scenario.status == "failed":
        attach(context.driver.get_screenshot_as_png(), attachment_type=attachment_type.PNG)


def after_all(context: Context):
    context.header_section.log_out()
    context.header_section.quite_driver()
