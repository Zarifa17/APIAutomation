import requests
import json
import jsonpath

def test_add_new_student():
    global id # id is local to one method hence make it global so that you can use it other methods
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("/Users/farhanmohammed/PycharmProjects/pythonPyTest/TestCases1/RequestJson.json", 'r')
    json_request = json.loads(file.read())
    response = requests.post(API_URL, json_request)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

def test_get_details():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response = requests.get(API_URL)
    print(response.text)
