# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.

import requests
import pytest
import allure

@allure.title("TC1 # Trying to verify firstname on a Patch request")
@allure.description("TC#1 -> Verify that Create Booking -> Patch Request - Verify that firstName is updated.")
@allure.tag("Integration", "p1")
@allure.label("Tester", "Suresh")
@allure.testcase("TC#1")
@pytest.mark.Integration
def test_patch_req(create_token, create_booking_id):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking_id)
    PATCH_URL = base_url + base_path
    print(PATCH_URL)
    cookie = "token=" + create_token
    print(cookie)
    headers = {"Content-Type": "application/json", "Accept": "application/json", "Cookie": cookie}
    print(headers)
    json_payload = {
        "firstname": "James",
        "lastname": "Brown",
    }
    print(json_payload)
    response = requests.patch(url=PATCH_URL, headers=headers, json=json_payload, verify=False)
    assert response.status_code == 200
    responseData = response.json()
    print(responseData)
    assert responseData["firstname"] == "James"
    assert responseData["lastname"] == "Brown"
