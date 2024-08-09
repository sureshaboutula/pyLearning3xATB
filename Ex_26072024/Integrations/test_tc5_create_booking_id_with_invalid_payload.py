# 5. Invalid Creation - enter a wrong payload or Wrong JSON.

import requests
import pytest
import allure

@allure.title("TC5 # Trying to Verify Create a booking with Invalid or empty payload")
@allure.description("TC#5 -> Invalid Creation - enter a wrong payload or Wrong JSON.")
@allure.tag("Integration", "p1")
@allure.label("Tester", "Suresh")
@allure.testcase("TC#5")
@pytest.mark.Integration
def test_create_booking_id_emptypayload():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    print(URL)
    headers = {"Content-Type": "application/json"}
    print(headers)
    payload = {
        # "firstname": "Jim",
        # "lastname": "Brown",
        # "totalprice": 111,
        # "depositpaid": True,
        # "bookingdates": {
        #     "checkin": "2023-08-04",
        #     "checkout": "2023-08-11"
        # },
        # "additionalneeds": "Lunch"
    }
    print(payload)
    response = requests.post(url=URL, headers=headers, json=payload, verify=False)
    assert response.status_code == 500


def test_create_booking_id_invalidheader():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    print(URL)
    headers = {"Content-Type": "application/xml"}
    print(headers)
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
    print(payload)
    response = requests.post(url=URL, headers=headers, json=payload, verify=False)
    assert response.status_code == 400

def test_create_booking_id_invalidpayload():
        base_url = "https://restful-booker.herokuapp.com"
        base_path = "/booking"
        URL = base_url + base_path
        print(URL)
        headers = {"Content-Type": "application/json"}
        print(headers)
        payload = {
            "firstname": "Jim",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2023-08-04",
                "checkout": "2023-08-11"
            },
            "additionalneeds": "Lunch"
        }
        print(payload)
        response = requests.post(url=URL, headers=headers, json=payload, verify=False)
        assert response.status_code != 200
