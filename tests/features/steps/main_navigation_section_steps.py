from behave import when
from behave.runner import Context


@when("I click [PIM] menu item in Main Navigation section")
def step_impl(context: Context):
    context.main_navigation_section.click_pim()


@when('I open "PIM" tab')
def step_impl(context: Context):
    context.main_navigation_section.click_pim()
