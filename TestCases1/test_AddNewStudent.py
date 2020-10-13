import requests
import json
import jsonpath

def test_addNewStudent():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("/Users/farhanmohammed/PycharmProjects/pythonPyTest/TestCases1/RequestJson.json", 'r')
    json_request = json.loads(file.read())
    response = requests.post(API_URL,json_request)
    print(response.text)

def test_getNewStudent():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/76101"
    response = requests.get(API_URL)
    #print(response.text)
    json_response = json.loads(response.text)   # Can also be written as  json_response=response.json()
    id = jsonpath.jsonpath(json_response,'data.id')
    print(id)
    assert id[0]==76101

def test_updateStudentData():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/76101"
    file = open("/Users/farhanmohammed/PycharmProjects/pythonPyTest/TestCases1/RequestJson.json", 'r')
    json_request = json.loads(file.read())
    response = requests.put(API_URL, json_request)
    print(response.text)

def test_getNewStudent():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/76101"
    response = requests.get(API_URL)
    json_response = json.loads(response.text)   # Can also be written as  json_response=response.json()
    print(json_response)
    id = jsonpath.jsonpath(json_response,'data.id')
    print(id)
    assert id[0]==76101

def test_deleteStudent():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/76101"
    response = requests.delete(API_URL)
    print(response.text)
