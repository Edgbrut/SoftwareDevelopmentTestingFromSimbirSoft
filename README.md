# Project description:
The project is testing 'demoqa.com/automation-practice-form' using Selenium Webdriver automation testing with Python. 
The goal of the project is to automate the testing of individual functions of the web application, 
such as filling out text boxes, select radio buttons, select dates in calendar, select checkboxes, 
upload pictures, select a dropdown.

# Major dependencies:
Python 3.10.11
Selenium 4.22.0
Pytest 8.2.2
Google Chrome Version 126.0.6478.182 
Allure version 2.26.0

# Instruction for running test:
For launching test: python -m pytest -s -v
For launching test with Allure Report: python -m pytest --alluredir=test_results/ tests/test_registration_page.py
To see Allure Report: allure serve test_results