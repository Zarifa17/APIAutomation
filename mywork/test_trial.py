import requests
import json
import jsonpath
#import pytest
from selenium import webdriver

# Steps for POST Method:
# 1. Read input from JSON file
# 2. Parse into JSON format
# 3. Hit Post Method
# 4. Parse response to JSON format
# 5. Validate Response

# API URL
url = "https://reqres.in/api/users"

# For Pytest create a method. This is 1 test case.
#@pytest.mark.skip("Dont want to execute with current build")
def test_create_new_user():
    file = open('/Users/farhanmohammed/PycharmProjects/pythonPyTest/mywork/createUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    response = requests.post(url, request_json)
    print(response.content)
    assert response.status_code == 201
    print(response.headers)
    print(response.headers.get('Content-Length'))
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])

# This is another test case
def test_create_other_user():
    file = open('/Users/farhanmohammed/PycharmProjects/pythonPyTest/mywork/createUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    response = requests.post(url, request_json)
    print(response.content)
    assert response.status_code == 201
    print(response.headers)
    print(response.headers.get('Content-Length'))
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])

def test_openBrowser():
    path = "/Users/farhanmohammed/PycharmProjects/pythonProject/drivers/chromedriver"
    driver = webdriver.Chrome(executable_path=path)
    driver.get("http://www.thetestingworld.com/testing")
    driver.maximize_window()