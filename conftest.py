import time
import pytest
import os
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def set_up(request):
    print("Start Test")
    # Create an instance of DesiredCapabilities
    capabilities = DesiredCapabilities.CHROME.copy()
    # Set the desired options
    capabilities["pageLoadStrategy"] = "eager"
    # Creating directory preferences and put the necessary settings in it. Universal path to download files
    preferences = {"download.default_directory": f"{os.getcwd()}/file_folder"}
    # Configure the Selenium webdriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", preferences)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    g = Service()
    # Pass the options to the Chrome driver
    driver = webdriver.Chrome(options=options, service=g)
    request.cls.driver = driver
    yield
    print("Finish Test")
    time.sleep(5)
    driver.quit()


@pytest.fixture(scope="module")
def set_group():
    print("Enter System")
    yield
    print("Exit System")
