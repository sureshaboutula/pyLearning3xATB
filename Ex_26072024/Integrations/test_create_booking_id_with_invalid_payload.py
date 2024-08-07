import requests
import pytest
import allure

def test_create_booking_id_emptypayload():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
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
    response = requests.post(url=URL, headers=headers, json=payload, verify=False)
    assert response.status_code == 500


def test_create_booking_id_invalidheader():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/xml"}
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
    assert response.status_code == 400

def test_create_booking_id_invalidpayload():
        base_url = "https://restful-booker.herokuapp.com"
        base_path = "/booking"
        URL = base_url + base_path
        headers = {"Content-Type": "application/json"}
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
        response = requests.post(url=URL, headers=headers, json=payload, verify=False)
        assert response.status_code != 200