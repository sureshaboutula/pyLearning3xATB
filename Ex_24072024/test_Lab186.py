import requests
import pytest
import allure


@allure.title("TC1 - Create Booking CRUD - Positive Case")
@allure.description("TC#1 -> Verify the Create Booking")
@allure.tag("Functional", "p0")
@allure.label("Tester", "Suresh")
@allure.testcase("TC#1")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    # URL
    # Method - Post
    # Headers - Content-Type: application/json
    # Payload - Data/Body - Dict/Json
    # Auth? - No

    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Suresh",
        "lastname": "Abo",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-08-04",
            "checkout": "2023-08-11"
        },
        "additionalneeds": "Lunch"
    }

    response = requests.post(url=URL, headers=headers, json=payload, verify=False)
    assert response.status_code == 200
    responseData = response.json()
    # Response body verification
    # Headers
    # Status Code
    # JSON Schema validation
    # Time Response

    assert responseData["bookingid"] != None
    assert responseData["bookingid"] > 0
    assert type(responseData["bookingid"]) == int
    fstname = responseData["booking"]["firstname"]
    lstname = responseData["booking"]["lastname"]
    assert fstname == "Suresh"
    assert lstname == "Abo"
    checkin = responseData["booking"]["bookingdates"]["checkin"]
    checkout = responseData["booking"]["bookingdates"]["checkout"]
    assert checkin == "2023-08-04"
    assert checkout == "2023-08-11"
    totalprice = responseData["booking"]["totalprice"]
    depositpaid = responseData["booking"]["depositpaid"]
    assert totalprice == 111
    assert depositpaid == True

    # print("JSON Response : \n", responseData.json())
    # print("Text Response : \n", responseData.text)
    # print("Header Information : ", responseData.headers)
    # print("Cookies : ", responseData.cookies)


#### Negative TC2
@allure.title("TC2 - Create Booking CRUD - Negative Case")
@allure.description("TC#2 -> Verify the Create Booking with empty payload")
@allure.tag("Functional", "p1")
@allure.label("Tester", "Suresh")
@allure.testcase("TC#2")
@pytest.mark.crud
def test_create_booking_negative_tc2():
    # URL
    # Method - Post
    # Headers - Content-Type: application/json
    # Payload - Data/Body - Dict/Json
    # Auth? - No

    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload = {}

    response = requests.post(url=URL, headers=headers, json=json_payload, verify=False)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))
    assert response.status_code == 500


#### Negative TC3
@allure.title("TC3 - Create Booking CRUD - Negative Case")
@allure.description("TC#3 -> Verify the Create Booking with totalprice value as string")
@allure.tag("Functional", "p1")
@allure.label("Tester", "Suresh")
@allure.testcase("TC#3")
@pytest.mark.crud
def test_create_booking_negative_tc3():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Suresh",
        "lastname": "Abo",
        "totalprice": "Test",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-08-04",
            "checkout": "2023-08-11"
        },
        "additionalneeds": "Lunch"
    }

    response = requests.post(url=URL, headers=headers, json=json_payload, verify=False)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))
    assert response.status_code == 200
    responseData = response.json()
    totalprice = responseData["booking"]["totalprice"]
    assert totalprice == None
