# 6. Trying to Update on a Delete Id -> 404

import requests
import pytest
import allure

@allure.title("TC6 # Trying to Update on a Delete Id")
@allure.description("TC#6 -> Verify PUT Request on a Deleted Id")
@allure.tag("Integration", "p1")
@allure.label("Tester", "Suresh")
@allure.testcase("TC#6")
@pytest.mark.Integration
def test_delete_req(create_token, create_booking_id):
    print("token", create_token)
    print("Delete Request Booking Id :", create_booking_id)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking_id)
    Delete_URl = base_url + base_path
    print(Delete_URl)
    cookie = "token=" + create_token
    print(cookie)
    headers = {"Content-Type": "application/json", "Cookie": cookie}
    print(headers)
    response = requests.delete(url=Delete_URl, headers=headers, verify=False)
    assert response.status_code == 201
    print("Deleted booking id is", create_booking_id)


def test_update_req(create_token, create_booking_id):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking_id)
    PUT_URL = base_url + base_path
    print(PUT_URL)
    cookie = "token=" + create_token
    print(cookie)
    headers = {"Accept": "application/json", "Cookie": cookie}
    print(headers)
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
    print(json_payload)
    response = requests.put(url=PUT_URL, headers=headers, json=json_payload, verify=False)
    assert response.status_code == 405
