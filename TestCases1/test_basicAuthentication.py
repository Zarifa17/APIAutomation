import requests
from requests.auth import HTTPBasicAuth


def test_basicAuthentication():
    response = requests.get('https://api.github.com/user',auth=HTTPBasicAuth('Zarifa17','Nyesha15!'))
    print(response.text)