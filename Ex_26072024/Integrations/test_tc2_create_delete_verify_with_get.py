# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.

import requests
import pytest
import allure

@allure.title("TC2 # Trying to GET details of Deleted Request")
@allure.description("TC#2 -> Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.")
@allure.tag("Integration", "p1")
@allure.label("Tester", "Suresh")
@allure.testcase("TC#2")
@pytest.mark.Integration
@pytest.mark.failed
def test_delete_req(create_token, create_booking_id):
    # token = create_token
    # booking_id = create_booking_id
    print("TC2", create_token)
    print("Delete Request Booking Id for TC2 :", create_booking_id)
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

def test_get_single_booking_id(create_booking_id):
    # booking_id = create_booking_id
    print("Get Request Booking Id", create_booking_id)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking_id)
    Get_URl = base_url + base_path
    print(Get_URl)
    headers = {"Accept": "application/json"}
    print(headers)
    response = requests.get(url = Get_URl, headers=headers, verify=False)
    assert response.status_code == 404


