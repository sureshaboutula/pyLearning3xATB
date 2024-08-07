
import pytest
import requests
import random

@pytest.fixture(scope="session")
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

@pytest.fixture(scope="session")
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

@pytest.fixture(scope="session")
def get_allbookings_req():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    Allurl = base_url + base_path

    response = requests.get(url=Allurl, verify=False)
    assert response.status_code == 200
    responseData = response.json()
    #print(responseData)
    return responseData

@pytest.fixture(scope="session")
def get_randon_bookingid_req():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    Allurl = base_url + base_path
    response = requests.get(url=Allurl, verify=False)
    assert response.status_code == 200
    responseData = response.json()
    # print(responseData)
    #bookingid_num = random.randint(0, len(get_allbookings_req))
    booking_id = responseData[random.randint(0, len(responseData))]["bookingid"]
    return booking_id


