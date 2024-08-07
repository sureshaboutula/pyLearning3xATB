# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.

import pytest
import requests
import random

# def test_get_single_id(get_randon_bookingid_req):
#     print(get_randon_bookingid_req)

def test_update_req_1(create_token, get_randon_bookingid_req):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(get_randon_bookingid_req)
    PUT_URL = base_url + base_path
    print(PUT_URL)
    cookie = "token=" + create_token
    print(cookie)
    headers = {"Accept": "application/json", "Cookie": cookie}
    json_payload = {
        "firstname": "TestFirst",
        "lastname": "TestLast",
        "totalprice": 211,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=PUT_URL, headers=headers, json=json_payload, verify=False)
    assert response.status_code == 200
    responseData = response.json()
    print(responseData)
    assert responseData["firstname"] == "TestFirst"
    assert responseData["lastname"] == "TestLast"
    assert responseData["bookingdates"]["checkin"] == "2018-01-01"
    assert responseData["bookingdates"]["checkout"] == "2019-01-01"
    assert responseData["totalprice"] == 211
    assert responseData["depositpaid"] == True
    assert responseData["additionalneeds"] == "Breakfast"

