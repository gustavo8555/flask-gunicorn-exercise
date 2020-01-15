import pytest
import requests
import json

url = 'http://127.0.0.1:5000'
headers = {'Content-Type': 'application/json'}

def test_post_gustavo():

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

def test_update_put():
    payload = {
    "nome": "gustavo lima",
    }

    r = requests.put(url+'/users/gustavo8555@hotmail.com', data=json.dumps(payload, indent=4), headers=headers)
    assert r.status_code == 200

    r = requests.get(url+'/users')
    data = r.json()
    assert data[0]['nome'] == 'gustavo lima'

def test_delete():
    r = requests.delete(url+'/users/gustavo8555@hotmail.com')
    assert r.status_code == 200
