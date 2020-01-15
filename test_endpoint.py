import pytest
import requests
import json

url = 'http://127.0.0.1:5000'


def test_post_gustavo():
    headers = {'Content-Type': 'application/json'}

    payload = {
    "nome": "gustavo",
    "email": "gustavo8555@hotmail.com",
    "telefones": [
        "11111"
    ]}

    r = requests.post(url+'/users', data=json.dumps(payload, indent=4), headers=headers)

    assert r.status_code == 200
    body = r.json()
    assert body['email'] == 'gustavo8555@hotmail.com'

def test_get():
    r = requests.get(url+'/users')
    data = r.json()

    assert r.status_code == 200
    assert data[0]['email'] == 'gustavo8555@hotmail.com'