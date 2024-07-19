import allure
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class StudentRegistrationForm(Base):

    # Launching the specified 'URL'
    base_url = 'https://demoqa.com/automation-practice-form'

    """Locators"""
    locator_first_name = "firstName"
    locator_last_name = "lastName"
    locator_reg_email = "//*[@id='userEmail']"
    locator_gender = "//label[@for='gender-radio-1']"
    locator_phone_number = "#userNumber"
    locator_dob = "//input[@id='dateOfBirthInput']"
    locator_year = "//select[@class='react-datepicker__year-select']"
    locator_month = "//select[@class='react-datepicker__month-select']"
    locator_date = "//div[@aria-label='Choose Friday, October 22nd, 1976']"
    locator_subject = "//*[@id='subjectsInput']"
    locator_subject_auto_complete_option = "//div[@id='react-select-2-option-0']"
    locator_file_upload = "//div[@class='form-file']//input[@type='file']"
    locator_address = "//*[@id='currentAddress']"
    locator_state = "//div[@id='state']"
    locator_uttar_pradesh_state = "//div[@id='react-select-3-option-1']"
    locator_city = "//div[@id='city']"
    locator_lucknow_city = "//div[@id='react-select-4-option-1']"
    locator_submit_btn = "//button[@id='submit']"

    # Locator of 'Page Title' after submitting registration form
    locator_page_title = "//div[@class='modal-title h4']"

    # Applicant information
    first_name = "Edgar"
    last_name = "Brutyan"
    email = "edbrutyan@yandex.ru"
    gender = "Male"
    phone_number = "1234567890"
    dob_date = "22"
    dob_month = "october"
    dob_year = "1976"
    subject = "Comp"
    subject_auto_complete_option = "Computer Science"
    address = "Russian Federation, city of Moscow"
    state = "Uttar Pradesh"
    city = "Lucknow"

    """Getters"""
    # Locating the elements using 'ID' locator for the text box 'First Name'
    def get_registration_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.locator_first_name)))

    # Locating the elements using 'ID' locator for the text box 'Last Name'
    def get_registration_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.locator_last_name)))

    # Locating the elements using 'XPATH' locator for the text box 'Email'
    def get_registration_reg_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_reg_email)))

    # Locating the elements using 'XPATH' locator for the radio button 'Gender'
    def get_registration_gender(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_gender)))

    # Locating the elements using 'CSS' locator for the text box 'Phone Number'
    def get_registration_mobile_num(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                self.locator_phone_number)))

    # Locating the elements using 'XPATH' locator for the text box 'DOB'
    def get_registration_dob(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_dob)))

    # Locating the elements using 'XPATH' locator for the text box 'Year'
    def get_registration_year(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_year)))

    # Locating the elements using 'XPATH' locator for the text box 'Month'
    def get_registration_month(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_month)))

    # Locating the elements using 'XPATH' locator for the text box 'Date'
    def get_registration_date(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_date)))

    # Locating the elements using 'XPATH' locator for the text box 'Subject'
    def get_registration_subject(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_subject)))

    # Locating the elements using 'XPATH' locator for the text box 'Subject auto complete option'
    def get_registration_computer_science_subject(self):
        return WebDriverWait(self.driver, 30)\
            .until(EC.element_to_be_clickable((By.XPATH, self.locator_subject_auto_complete_option)))

    # Locating the elements using 'XPATH' locator for the button 'File Upload'
    def get_registration_file_upload(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.locator_file_upload)))

    # Locating the elements using 'XPATH' locator for the text box 'Current Address'
    def get_registration_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_address)))

    # Locating the elements using 'XPATH' locator for dropdown 'State'
    def get_registration_state(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_state)))

    # Locating the elements using 'XPATH' locator for dropdown 'Selected State Uttar Pradesh'
    def get_registration_uttar_pradesh_state(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.locator_uttar_pradesh_state)))

    # Locating the elements using 'XPATH' locator for dropdown 'City'
    def get_registration_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_city)))

    # Locating the elements using 'XPATH' locator for dropdown 'Selected City Lucknow'
    def get_registration_lucknow_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.locator_lucknow_city)))

    # Locating the elements using 'XPATH' locator for the button 'Submit'
    def get_registration_submit_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.locator_submit_btn)))

    # Locating the elements using 'XPATH' locator for the popup modal-title 'Thanks for submitting the form'
    def get_registration_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.locator_page_title)))

    """Actions"""
    # First Name Field
    def input_registration_first_name(self, first_name):
        self.get_registration_first_name().send_keys(first_name)
        print(f"First Name: {first_name}")

    # Last Name Field
    def input_registration_last_name(self, last_name):
        self.get_registration_last_name().send_keys(last_name)
        print(f"Last Name: {last_name}")

    # Email Name Field
    def input_registration_reg_email(self, reg_email):
        self.get_registration_reg_email().send_keys(reg_email)
        print(f"Email: {reg_email}")

    # Select a Gender 'Male'
    def click_registration_gender(self):
        # Calling Method from Base
        self.get_btn_selected(self.get_registration_gender(), self.gender)

    # Mobile Number Field
    def input_registration_mobile_num(self, mobile_num):
        self.get_registration_mobile_num().send_keys(mobile_num)
        print(f"Phone Number: {mobile_num}")

    # DOB Calendar Picker
    def click_registration_dob(self):
        self.get_registration_dob().click()
        print("Click on Calendar")

    # Select a Year on Calendar
    def click_registration_year(self, dob_year):
        ry = Select(self.get_registration_year())
        ry.select_by_value(dob_year)
        print(f"Selected Year: {dob_year}")

    # Select a Month on Calendar
    def click_registration_month(self, dob_month):
        rm = Select(self.get_registration_month())
        rm.select_by_value("9")
        print(f"Selected Month: {dob_month}")

    # Select a Date on Calendar
    def click_registration_date(self, dob_date):
        self.get_registration_date().click()
        print(f"Selected Date: {dob_date}")

    # Click on Subject Field and Write 'Comp'
    def input_registration_subject(self, subject):
        self.get_registration_subject().send_keys(subject)
        print(f"Subject Field: {subject}")

    # Choose Computer Science in Subject Field
    def click_registration_computer_science_subject(self, subject_auto_complete_option):
        self.get_registration_computer_science_subject().click()
        print(f"Subject: {subject_auto_complete_option}")

    # Upload a File
    def input_registration_file_upload(self):
        # Absolute path to the directory from where the file is uploaded
        self.get_registration_file_upload().send_keys(f"{os.getcwd()}/file_folder/Simbirsoft.jpg")
        print("File Uploaded Successfully")

    # Current Address Field
    def input_registration_address(self, address):
        self.get_registration_address().send_keys(address)
        print(f"Inserted Address: {address}")

    # State Dropdown
    def click_registration_state(self):
        self.get_registration_state().click()
        print("Click on State Dropdown")

    # Select an 'Uttar Pradesh' State
    def click_registration_uttar_pradesh_state(self, state):
        self.get_registration_uttar_pradesh_state().click()
        print(f"Selected State: {state}")

    # City Dropdown
    def click_registration_city(self):
        self.get_registration_city().click()
        print("Click on City Dropdown")

    # Select a 'Lucknow' City
    def click_registration_lucknow_city(self, city):
        self.get_registration_lucknow_city().click()
        print(f"City: {city}")

    # Click on 'Submit' Button
    def click_registration_submit_btn(self):
        self.get_registration_submit_btn().submit()
        print("Click on Submit Button")

    """Methods"""
    # Submit Student Registration Form
    def submit_application(self):
        # Allure Reports
        with allure.step("submit_form_report"):
            # Getting website address
            self.driver.get(self.base_url)
            # Calling Method from Base 'Get Current URL'
            self.get_current_url()
            # Calling Method from Base 'Assert URL'
            self.get_assert_url(self.base_url)
            # Maximizing Window
            self.driver.maximize_window()
            # Input First Name
            self.input_registration_first_name(self.first_name)
            # Input Last Name
            self.input_registration_last_name(self.last_name)
            # Input Email
            self.input_registration_reg_email(self.email)
            # Select Gender
            self.click_registration_gender()
            # Input Phone Number
            self.input_registration_mobile_num(self.phone_number)
            # Click on Calendar
            self.click_registration_dob()
            # Select Year
            self.click_registration_year(self.dob_year)
            # Select Month
            self.click_registration_month(self.dob_month)
            # Select Date
            self.click_registration_date(self.dob_date)
            # Input Subject Name
            self.input_registration_subject(self.subject)
            # Click on Subject Name
            self.click_registration_computer_science_subject(self.subject_auto_complete_option)
            # Upload Image
            self.input_registration_file_upload()
            # Input Address
            self.input_registration_address(self.address)
            # Scrolling Page Down (because in some monitors 'State and City' staying in bottom and not reachable)
            self.driver.execute_script("window.scrollTo(0, 1000)")
            # Click on State Dropdown
            self.click_registration_state()
            # Select a State
            self.click_registration_uttar_pradesh_state(self.state)
            # Click on City Dropdown
            self.click_registration_city()
            # Select a City
            self.click_registration_lucknow_city(self.city)
            # Click on Submit Button
            self.click_registration_submit_btn()
            # Calling Method from Base to Assert Popup 'Submitting' Form
            self.assert_word(self.get_registration_page_title(), "Thanks for submitting the form")
            # Calling Method from Base 'Screenshot'
            self.get_screenshot()
