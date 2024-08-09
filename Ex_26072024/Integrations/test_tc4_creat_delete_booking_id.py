# 4. Create a BOOKING, Delete It

import requests
import pytest
import allure

@allure.title("TC4 # Trying to Delete a newly created booking")
@allure.description("TC#4 -> Verify Delete Request on a Created Booking")
@allure.tag("Integration", "p1")
@allure.label("Tester", "Suresh")
@allure.testcase("TC#4")
@pytest.mark.Integration
def test_delete_req(create_token, create_booking_id):
    # token = create_token
    # booking_id = create_booking_id
    print("TC4", create_token)
    print("Delete Request Booking Id for TC4 :", create_booking_id)
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
