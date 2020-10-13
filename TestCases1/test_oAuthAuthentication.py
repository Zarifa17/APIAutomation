import requests
import json
import jsonpath

def test_oAuth_Api():
    token_url = "http://thetestingworlapi.com/Token"
    data={'grant_type':'password','username':'admin','password':''} # cannot complete this tc since lecturer didnt give PW details.This test case wont run.
    response=requests.post(token_url,data)
    token_value=jsonpath.jsonpath(response.json(),'access_token')

    auth={'Authorization':'Bearer '+token_value[0]}
    API_URL = "http://thetestingworldapi.com/api/StDetails/76102"
    response=requests.get(API_URL, headers=auth)
    print(response.text)


# Cannot complete this tc since lecturer didnt give PW details.This test case wont run.