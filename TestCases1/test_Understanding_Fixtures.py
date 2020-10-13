from selenium.webdriver import Chrome

import pytest
#@pytest.fixture(scope="module) ---> Only one browser will start & will close at the end after all the below test cases are executed

@pytest.fixture()
def setPath():    # This is a fixture
    global driver
    path = "/Users/farhanmohammed/PycharmProjects/pythonProject/drivers/chromedriver"
    driver = Chrome(executable_path=path)
    yield     # yield will tell what code i want to execute after all the test execution
    #driver.close()

def test_registration_valid_data(setPath):  # Test Case 1
    driver.get("http://www.thetestingworld.com/testing")
    driver.maximize_window()
    assert driver.current_url == "https://www.thetestingworld.com/testing"

def test_registration_invalid_data(setPath):   # Test Case 2
    driver.get("http://www.thetestingworld.com/testing")
    driver.maximize_window()

def test_invalid_data(setPath):   # Test Case 3
    driver.get("http://www.thetestingworld.com/testing")
    driver.maximize_window()