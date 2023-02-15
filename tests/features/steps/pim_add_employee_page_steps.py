from behave import step
from behave.runner import Context


@step('I fill name "{test_user_name}" and last name "{test_user_lastname}" in Add Employee page and click Save button')
def step_impl(context: Context, test_user_name: str, test_user_lastname: str):
    context.pim_add_employee_page.add_employee(test_user_name=test_user_name, test_user_lastname=test_user_lastname)
