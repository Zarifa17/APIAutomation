import requests
import jsonpath
import json


def test_add_new_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("/Users/farhanmohammed/PycharmProjects/pythonPyTest/TestCases1/RequestJson.json", 'r')
    json_request = json.loads(file.read())
    response = requests.post(API_URL,json_request)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    Tech_API_URL = "http://thetestingworldapi.com/api/technicalskills"
    file = open("/Users/farhanmohammed/PycharmProjects/pythonPyTest/TestCases1/Techdetails.json",'r')
    json_request = json.loads(file.read())
    json_request['id']=int(id[0])
    json_request['st_id']=id[0]
    response = requests.post(Tech_API_URL,json_request)
    print(response.text)

    Address_API_URL = "http://thetestingworldapi.com/api/addresses"
    file = open("/Users/farhanmohammed/PycharmProjects/pythonPyTest/TestCases1/AddressDetails.json",'r')
    json_request = json.loads(file.read())
    json_request['stId']=id[0]
    response = requests.post(Address_API_URL,json_request)

    final_details = "http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(final_details)
    print(response.status_code)
    print(response.text)

