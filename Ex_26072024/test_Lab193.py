
import requests
import allure

### Below code is moved to conftest.py file
# @pytest.fixture()
# def create_token():
#     url = "https://restful-booker.herokuapp.com/auth"
#     headers = {"Content-Type": "application/json"}
#     json_payload = {
#         "username": "admin",
#         "password": "password123"
#     }
#     response = requests.post(url=url, json=json_payload, headers=headers, verify=False)
#     token = response.json()["token"]
#     print(token)
#     return token
#
# @pytest.fixture()
# def create_booking_id():
#     base_url = "https://restful-booker.herokuapp.com"
#     base_path = "/booking"
#     URL = base_url + base_path
#     headers = {"Content-Type": "application/json"}
#     payload = {
#         "firstname": "Jim",
#         "lastname": "Brown",
#         "totalprice": 111,
#         "depositpaid": True,
#         "bookingdates": {
#             "checkin": "2023-08-04",
#             "checkout": "2023-08-11"
#         },
#         "additionalneeds": "Lunch"
#     }
#     response = requests.post(url=URL, headers=headers, json=payload, verify=False)
#     # assert response.status_code == 200
#     responseData = response.json()
#     booking_id = responseData["bookingid"]
#     return booking_id


def test_update_req_1(create_token, create_booking_id):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking_id)
    PUT_URL = base_url + base_path
    print(PUT_URL)
    cookie = "token=" + create_token
    print(cookie)
    headers = {"Accept": "application/json", "Cookie": cookie}
    json_payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 211,
        "depositpaid": False,
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
    fstname = responseData["firstname"]
    lstname = responseData["lastname"]
    assert fstname == "James"
    assert lstname == "Brown"
    checkin = responseData["bookingdates"]["checkin"]
    checkout = responseData["bookingdates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"
    totalprice = responseData["totalprice"]
    depositpaid = responseData["depositpaid"]
    assert totalprice == 211
    assert depositpaid == False
    additionalneeds = responseData["additionalneeds"]
    assert additionalneeds == "Breakfast"


def test_delete_req_2(create_token, create_booking_id):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking_id)
    Delete_URl = base_url + base_path
    print(Delete_URl)
    cookie = "token=" + create_token
    print(cookie)
    headers = {"Content-Type": "application/json", "Cookie": cookie}

    response = requests.delete(url=Delete_URl, headers=headers, verify=False)
    assert response.status_code == 201