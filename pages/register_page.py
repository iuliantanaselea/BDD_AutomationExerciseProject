from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.common.action_chains import ActionChains
from browser import Browser


class RegisterPage(Browser):
    APP_LOGO = (By.CSS_SELECTOR, '[alt=\"Website for automation practice\"]')
    SIGNUP_LOGIN_BUTTON = (By.CSS_SELECTOR, '[href=\"/login\"]')
    NEW_USER_SIGNUP_MESSAGE = (By.XPATH, '//div[@class=\"signup-form\"]//h2')
    NAME_FIELD = (By.CSS_SELECTOR, '[data-qa=\"signup-name\"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, '[data-qa=\"signup-email\"]')
    SIGNUP_BUTTON = (By.CSS_SELECTOR, '[data-qa=\"signup-button\"]')
    ENTER_ACCOUNT_INFORMATION_MESSAGE = (By.CSS_SELECTOR, 'div>h2>b')
    TITLE_FIELD = (By.CSS_SELECTOR, '[for=\"id_gender1\"]')
    PASSWORD_FIELD = (By.ID, 'password')
    DATE_OF_BIRTH_DAY_OBJECT = (By.ID, 'days')
    DATE_OF_BIRTH_MONTH_OBJECT = (By.ID, 'months')
    DATE_OF_BIRTH_YEAR_OBJECT = (By.ID, 'years')
    NEWSLETTER_CHECKBOX_OBJECT = (By.XPATH, '//input[@id=\"newsletter\"]')
    SPECIAL_OFFERS_CHECKBOX_OBJECT = (By.ID, 'optin')
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '[data-qa=\"first_name\"]')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '[data-qa=\"last_name\"]')
    COMPANY_FIELD = (By.CSS_SELECTOR, '[data-qa=\"company\"]')
    ADDRESS_FIELD = (By.CSS_SELECTOR, '[data-qa=\"address\"]')
    ADDRESS2_FIELD = (By.CSS_SELECTOR, '[data-qa=\"address2\"]')
    COUNTRY_FIELD = (By.CSS_SELECTOR, '[data-qa=\"country\"]')
    STATE_FIELD = (By.CSS_SELECTOR, '[data-qa=\"state\"]')
    CITY_FIELD = (By.CSS_SELECTOR, '[data-qa=\"city\"]')
    ZIPCODE_FIELD = (By.CSS_SELECTOR, '[data-qa=\"zipcode\"]')
    MOBILE_NUMBER_FIELD = (By.CSS_SELECTOR, '[data-qa=\"mobile_number\"]')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//button[@data-qa=\"create-account\"]')
    ACCOUNT_CREATED_MESSAGE = (By.CSS_SELECTOR, '[data-qa=\"account-created\"]')
    CONTINUE_BUTTON = (By.XPATH, '//div/a[contains(text(),\"Continue\")]')
    # CONTINUE_BUTTON = (By.CSS_SELECTOR, '[data-qa=\"continue-button\"]')
    LOGGED_IN_AS_USERNAME_MESSAGE = (By.XPATH, '//li/a[contains(text(),\" Logged in as\")]')
    DELETE_ACCOUNT_BUTTON = (By.XPATH, '//li/a[contains(text(),\" Delete Account\")]')
    ACCOUNT_DELETED_MESSAGE = (By.CSS_SELECTOR, '[data-qa=\"account-deleted\"]')
    AD_CLOSE_BUTTON = (By.XPATH, '//div[@aria-label=\"Close ad\"]')
    EMAIL_EXISTS_MESSAGE = (By.XPATH, '//p[contains(text(),\"Email Address already exist!\")]')
    name = "Mark"
    random_number_1 = random.randint(1, 999999)  # genereaza un numar aleator intre 1 si 999999
    def go_to_main_page(self):
        self.driver.get("https://automationexercise.com/")

    def get_app_logo(self):
        app_logo = self.driver.find_element(*self.APP_LOGO)
        assert app_logo.is_displayed()

    def click_signup_login_button(self):
        self.driver.find_element(*self.SIGNUP_LOGIN_BUTTON).click()

    def get_new_user_signup_message(self):
        try:
            return self.driver.find_element(*self.NEW_USER_SIGNUP_MESSAGE)
        except NoSuchElementException:
            return False

    def set_name_object(self):
        self.driver.find_element(*self.NAME_FIELD).send_keys(self.name)

    def set_email_object(self):

        self.driver.find_element(*self.EMAIL_FIELD).send_keys(f"Mark{self.random_number_1}@exercise.com")

    def set_existing_email_object(self):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(f"Mark{self.random_number_1}@exercise.com")
    def click_signup_button(self):
        signup_button = self.driver.find_element(*self.SIGNUP_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", signup_button)
        signup_button.click()

    def get_enter_account_information_message(self):
        enter_account_information_message = self.driver.find_element(*self.ENTER_ACCOUNT_INFORMATION_MESSAGE)
        self.assertEqual(enter_account_information_message.text,
                         "ENTER ACCOUNT INFORMATION",
                         "Message not displayed")

    def set_primary_details(self):
        self.driver.find_element(*self.TITLE_FIELD).click()
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys("password")
        day_of_birth_element = self.driver.find_element(*self.DATE_OF_BIRTH_DAY_OBJECT)
        day_of_birth = Select(day_of_birth_element)
        day_of_birth.select_by_value("20")
        month_of_birth_element = self.driver.find_element(*self.DATE_OF_BIRTH_MONTH_OBJECT)
        month_of_birth = Select(month_of_birth_element)
        month_of_birth.select_by_visible_text("May")
        year_of_birth_element = self.driver.find_element(*self.DATE_OF_BIRTH_YEAR_OBJECT)
        year_of_birth = Select(year_of_birth_element)
        year_of_birth.select_by_value("1994")

    def select_sign_up_for_newsletter_checkbox(self):
        newsletter_button = self.driver.find_element(*self.NEWSLETTER_CHECKBOX_OBJECT)
        self.driver.execute_script("arguments[0].scrollIntoView();", newsletter_button)
        newsletter_button.click()

    def select_receive_special_offers_checkbox(self):
        self.driver.find_element(*self.SPECIAL_OFFERS_CHECKBOX_OBJECT).click()

    def set_secondary_details(self):
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys("Mark")
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys("Twain")
        self.driver.find_element(*self.COMPANY_FIELD).send_keys("Freelancer")
        self.driver.find_element(*self.ADDRESS_FIELD).send_keys("Washington Str, 10340")
        country_selector_element = self.driver.find_element(*self.COUNTRY_FIELD)
        country = Select(country_selector_element)
        country.select_by_value("United States")

        self.driver.find_element(*self.STATE_FIELD).send_keys("Washington")
        self.driver.find_element(*self.CITY_FIELD).send_keys("Washington DC")
        self.driver.find_element(*self.ZIPCODE_FIELD).send_keys("102340")
        self.driver.find_element(*self.MOBILE_NUMBER_FIELD).send_keys("4032023492")

    def click_create_account_button(self):
        create_account_button = self.driver.find_element(*self.CREATE_ACCOUNT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", create_account_button)
        create_account_button.click()

    def get_account_created_message(self):
        get_account_created_message = self.driver.find_element(*self.ACCOUNT_CREATED_MESSAGE)
        self.assertEqual(get_account_created_message.text,
                         "ACCOUNT CREATED!",
                         "Message not displayed")

    def click_continue_button(self):
        # self.driver.refresh()
        continue_button = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa=\"continue-button\"]')))
        continue_button.click()
        # self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_logged_in_as_username_message(self):
        self.driver.refresh()
        # WebDriverWait(self.driver, 5)
        actions = ActionChains(self.driver)
        actions.move_to_element(
            self.driver.find_element(By.XPATH, '//div/a[contains(text(),\"Continue\")]')).click().perform()
        # actions.move_by_offset(0, 0).click().perform()


        logged_in_as_message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.LOGGED_IN_AS_USERNAME_MESSAGE)))
        # logged_in_as_message = self.driver.find_element(*self.LOGGED_IN_AS_USERNAME_MESSAGE)
        self.assertEqual(logged_in_as_message.text,
                         f"Logged in as {self.name}"
                         , "Text not displayed correctly")

    def click_delete_account_button(self):
        self.driver.find_element(*self.DELETE_ACCOUNT_BUTTON).click()

    def get_account_deleted_message(self):
        account_deleted_message = self.driver.find_element(*self.ACCOUNT_DELETED_MESSAGE)
        self.assertEqual(account_deleted_message.text,
                         "ACCOUNT DELETED!",
                         "Message not displayed")

    def delete_cookies(self):
        self.driver.delete_all_cookies()

    def get_email_already_exists_error_message(self):
        email_exists_message = self.driver.find_element(*self.EMAIL_EXISTS_MESSAGE)
        self.assertEqual(email_exists_message.text,
                         "Email Address already exist!",
                         'Message not displayed')

