import requests
import json
import jsonpath
import openpyxl
from DataDriven import Library

def test_add_mulitple_data():
    #API
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("/Users/farhanmohammed/PycharmProjects/pythonPyTest/TestCases1/RequestJson.json",'r')
    json_request = json.loads(file.read())

    obj = Library.Common('/Users/farhanmohammed/PycharmProjects/pythonPyTest/TestCases1/TestData.xlsx', 'Sheet1') # Need to pass 2 arguments FileNamePath & SheetName
    col = obj.fetch_coulumn_count()
    row = obj.fetch_row_count()
    keylist = obj.fetch_key_name()


    for i in range(2,row+1):
        updated_json_request = obj.update_json_request(i,json_request,keylist)
        response = requests.post(API_URL,updated_json_request)
        print(response)