from behave import *


@given('I am on the https://automationexercise.com/ page')
def step_impl(context):
    context.register_page_object.go_to_main_page()


@then('Home page should be visible successfully')
def step_impl(context):
    context.register_page_object.get_app_logo()


@when('I click on "Signup / Login" button')
def step_impl(context):
    context.register_page_object.click_signup_login_button()


@then('"New User Signup!" should be visible')
def step_impl(context):
    context.register_page_object.get_new_user_signup_message()


@when('I enter name')
def step_impl(context):
    context.register_page_object.set_name_object()


@when('I enter email')
def step_impl(context):
    context.register_page_object.set_email_object()


@when('I click "Signup" button')
def step_impl(context):
    context.register_page_object.click_signup_button()


@then('"ENTER ACCOUNT INFORMATION" should be visible')
def step_impl(context):
    context.register_page_object.get_enter_account_information_message()


@when('I fill details: Title, Name, Email, Password, Date of birth')
def step_impl(context):
    context.register_page_object.set_primary_details()


@when('I select checkbox "Sign up for our newsletter!"')
def step_impl(context):
    context.register_page_object.select_sign_up_for_newsletter_checkbox()


@when('I select checkbox "Receive special offers from our partners!"')
def step_impl(context):
    context.register_page_object.select_receive_special_offers_checkbox()


@when('I fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number')
def step_impl(context):
    context.register_page_object.set_secondary_details()


@when('I click "Create Account button"')
def step_impl(context):
    context.register_page_object.click_create_account_button()


@then('"ACCOUNT CREATED!" should be visible')
def step_impl(context):
    context.register_page_object.get_account_created_message()


@when('I click "Continue" button')
def step_impl(context):
    context.register_page_object.click_continue_button()


@then('"Logged in as username" should visible')
def step_impl(context):
    context.register_page_object.get_logged_in_as_username_message()


@when('I click "Delete Account" button')
def step_impl(context):
    context.register_page_object.click_delete_account_button()


@then('"ACCOUNT DELETED!" should be visible')
def step_impl(context):
    context.register_page_object.get_account_deleted_message()

@when('I delete cookies')
def steps_impl(context):
    context.register_page_object.delete_cookies()

@when('I Enter name and already registered email address')
def steps_impl(context):
    context.register_page_object.set_name_object()
    context.register_page_object.set_existing_email_object()

@then('"Email Address already exist!" should be visible')
def steps_impl(context):
    context.register_page_object.get_email_already_exists_error_message()

@when('I go to main page')
def steps_impl(context):
    context.register_page_object.go_to_main_page()