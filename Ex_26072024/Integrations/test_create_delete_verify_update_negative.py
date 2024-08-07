# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.

import requests

def test_delete_req(create_token, create_booking_id):
    token = create_token
    booking_id = create_booking_id
    print(token)
    print("Delete Request Booking Id :", booking_id)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(booking_id)
    Delete_URl = base_url + base_path
    print(Delete_URl)
    cookie = "token=" + token
    print(cookie)
    headers = {"Content-Type": "application/json", "Cookie": cookie}

    response = requests.delete(url=Delete_URl, headers=headers, verify=False)
    assert response.status_code == 201

def test_update_req(create_token, create_booking_id):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking_id)
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
    assert response.status_code == 405
