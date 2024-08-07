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

def test_get_single_booking_id(create_booking_id):
    booking_id = create_booking_id
    print("Get Request Booking Id", booking_id)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(booking_id)
    Get_URl = base_url + base_path
    print(Get_URl)
    headers = {"Accept": "application/json"}
    response = requests.get(url = Get_URl, headers=headers, verify=False)
    assert response.status_code == 404


