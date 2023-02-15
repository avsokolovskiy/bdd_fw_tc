from behave import step, then, when
from behave.runner import Context
from hamcrest import assert_that, equal_to


@step("I click [Add] button in PIM employee list page")
def step_impl(context: Context):
    context.pim_employee_list_page.click_add_button()


@step('I enter user name "{test_user_name}" and lastname "{test_user_lastname}" '
      'in the search field in PIM employee list page')
def step_impl(context: Context, test_user_name: str, test_user_lastname: str):
    context.pim_employee_list_page.fill_search_form(field_name=test_user_name,
                                                    field_value=test_user_lastname)


@step("I click the [Search] button in PIM employee list page")
def step_impl(context: Context):
    context.pim_employee_list_page.click_search_button()


@then('Created employee name "{test_user_name}" and last name "{test_user_lastname}" '
      'are present in PIM employee list page')
def step_impl(context: Context, test_user_name: str, test_user_lastname: str):
    employee_actual_name = context.pim_employee_list_page.get_user_name()
    employee_actual_lastname = context.pim_employee_list_page.get_user_lastname()
    assert_that(employee_actual_name, equal_to(test_user_name))
    assert_that(employee_actual_lastname, equal_to(test_user_lastname))


@step('I enter 3 letters of user name "{test_user_name}" in the search field in PIM employee list page')
def step_impl(context: Context, test_user_name: str):
    context.pim_employee_list_page.fill_search_form(field_name=f'{test_user_name}'[:3],
                                                    field_value='')


@step('I click auto-suggest list element with name "{test_user_name}" and last name "{test_user_last_name}"')
def step_impl(context: Context, test_user_name: str, test_user_last_name: str):
    context.pim_employee_list_page.click_employee_autosuggest_list_element(test_user_name=test_user_name,
                                                                           test_user_last_name=test_user_last_name)


@then("search result is (1) Record Found")
def step_impl(context: Context):
    assert_that(context.pim_employee_list_page.check_if_search_results_qty_1())


@when("I click [trash] button")
def step_impl(context: Context):
    context.pim_employee_list_page.click_trash_button()


@step("I click [delete] button")
def step_impl(context: Context):
    context.pim_employee_list_page.click_delete_yes_button()


@then("search result is No Records Found")
def step_impl(context: Context):
    assert_that(context.pim_employee_list_page.check_if_search_results_empty())


@when("I click [Pencil] button")
def step_impl(context: Context):
    context.pim_employee_list_page.click_pencil_button()


@then('employee Job title "{test_job_title}" is present in employee line')
def step_impl(context: Context, test_job_title: str):
    job_title_ext = context.pim_employee_list_page.get_user_job_title()
    assert_that(job_title_ext, equal_to(test_job_title))


@step("I add new employee")
def step_impl(context: Context):
    context.pim_employee_list_page.click_add_button()
    for row in context.table:
        context.pim_add_employee_page.fill_input_field(field_name=row["INFO"], field_value=row["VALUE"])
    context.pim_add_employee_page.click_save_button()


@step("I search for employee")
def step_impl(context: Context):
    for row in context.table:
        context.pim_employee_list_page.fill_search_form(field_name=row["INFO"], field_value=row["VALUE"])
    context.pim_employee_list_page.click_search_button()


@then("Employee record is found")
def step_impl(context: Context):
    assert_that(context.pim_employee_list_page.check_if_search_results_qty_1())
    for row in context.table:
        actual_column_value = context.pim_employee_list_page.get_cell_text(column_name=row["COLUMN"])
        assert_that(actual_column_value, equal_to(row["VALUE"]), f"Mismatch on [{row['COLUMN']}]")


@when("I update job title to '{new_job_title}'")
def step_impl(context: Context, new_job_title: str):
    context.pim_employee_list_page.click_pencil_button()
    context.pim_employee_details_page.click_job_menu_item()
    context.pim_employee_details_page.click_job_title_dropdown()
    context.pim_employee_details_page.click_selected_job_title(job_title=new_job_title)
    context.pim_employee_details_page.click_joined_date_dropdown()
    context.pim_employee_details_page.click_today_button()
    context.pim_employee_details_page.click_save_button()


@step('I search for employee by entering "3" symbols of his name and selecting him in auto-suggest list')
def step_impl(context: Context):
    for row in context.table:
        context.pim_employee_list_page.fill_search_form(field_name=row["INFO"], field_value=row["VALUE"][:3])
        context.pim_employee_list_page.click_employee_autosuggest_list_element(test_user_name=row["VALUE"])
    context.pim_employee_list_page.click_search_button()

@when("I delete the founded employee")
def step_impl(context: Context):
    context.pim_employee_list_page.click_trash_button()
    context.pim_employee_list_page.click_delete_yes_button()


@then("Employee record is NOT found")
def step_impl(context: Context):
    assert_that(context.pim_employee_list_page.check_if_search_results_empty())
