
import pytest
import requests
import random

@pytest.fixture(scope="module")
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, json=json_payload, headers=headers, verify=False)
    assert response.status_code == 200
    assert response.json()["token"] != None
    token = response.json()["token"]
    print(token)
    return token

@pytest.fixture(scope="module")
def create_booking_id():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-08-04",
            "checkout": "2023-08-11"
        },
        "additionalneeds": "Lunch"
    }
    response = requests.post(url=URL, headers=headers, json=payload, verify=False)
    assert response.status_code == 200
    responseData = response.json()
    assert responseData["bookingid"] != None
    booking_id = responseData["bookingid"]
    return booking_id

@pytest.fixture(scope="module")
def get_allbookings_req():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    Allurl = base_url + base_path
    response = requests.get(url=Allurl, verify=False)
    assert response.status_code == 200
    responseData = response.json()
    return responseData


