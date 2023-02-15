from behave import then, when, step
from behave.runner import Context
from hamcrest import assert_that


@then("PIM Personal Details page is displayed")
def step_impl(context: Context):
    employee_details_is_displayed = context.pim_employee_details_page.check_if_details_page_is_displayed()
    assert_that(employee_details_is_displayed)


@when("I click [Job] menu item")
def step_impl(context: Context):
    context.pim_employee_details_page.click_job_menu_item()


@step("click [job title field] dropdown button")
def step_impl(context: Context):
    context.pim_employee_details_page.click_job_title_dropdown()


@step('select "{job_title}"')
def step_impl(context: Context, job_title: str):
    context.pim_employee_details_page.click_selected_job_title(job_title=job_title)


@step("click [calendar] button in Joined Date field")
def step_impl(context: Context):
    context.pim_employee_details_page.click_joined_date_dropdown()


@step("click [Today] button")
def step_impl(context: Context):
    context.pim_employee_details_page.click_today_button()


@step("click [Save] button")
def step_impl(context: Context):
    context.pim_employee_details_page.click_save_button()


@then("New Employee Personal Details page is displayed")
def step_impl(context: Context):
    personal_assertions = {
        "Full Name": context.pim_employee_details_page.check_if_employee_full_name_is_displayed
    }
    assert_that(context.pim_employee_details_page.check_if_details_page_is_displayed())
    for row in context.table:
        assert_that(personal_assertions[row["INFO"]](personal_data=row["VALUE"]))
