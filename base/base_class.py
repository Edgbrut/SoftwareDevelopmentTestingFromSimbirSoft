import datetime
import time
import os


class Base:
    def __init__(self, driver):
        self.driver = driver

    """Method Get Current URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current URL: {get_url}")

    """Method Assert URL"""
    def get_assert_url(self, result):
        get_url = self.driver.current_url
        # assertion url
        assert get_url == result
        print("URL Assertion Confirmed")

    """Method Assert Word"""
    @staticmethod
    def assert_word(word, result):
        value_word = word.text
        # assertion page name
        assert value_word == result
        print(f"Page Name Assertion: {value_word}")

    """Method Screenshot"""
    def get_screenshot(self):
        time.sleep(3)
        # getting the current time in UTC time zone and converting date and time into a string in the specified format.
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M")
        name_screenshot = 'screenshot_' + now_date + '.png'
        # with 'os.path.join(os.getcwd())' returns the full path to the current working directory
        self.driver.save_screenshot(f"{os.path.join(os.getcwd())}/screen/" + name_screenshot)
        print(f"Screenshot Complete: {name_screenshot}")

    """Method Check If Button Or CheckBox Selected And Assertion"""
    @staticmethod
    def get_btn_selected(btn, name):
        value_btn = btn
        name_btn = value_btn.text
        # assertion button name
        assert name_btn == name
        print(f"Button Name Assertion: {name_btn}")
        # with if-else statement checking if button is selected
        if value_btn.is_selected():
            pass
            print(f"'{name_btn}' Button Is Selected")
        else:
            value_btn.click()
            print(f"Gender: {name_btn}")
