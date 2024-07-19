import pytest
import allure
from pages.registration_form_page import StudentRegistrationForm


@pytest.mark.usefixtures("set_up")
@allure.description("Test Student Registration Form")
class TestRegistrationForm:

    def test_registration_page(self, set_group):

        # Submit Student Application Form
        rf = StudentRegistrationForm(self.driver)
        rf.submit_application()
        print("Thanks for submitting the form!")
