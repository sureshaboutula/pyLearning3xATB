# Request Module -->
# Module -> Package or Library contains functions which you can use easily
# Example : math, pytest, os, csv, allure, etc

# Request Module --> To make HTTP methods
# GET, POST, PUT, PATCH, DELETE, OPTIONS....
# URL, Auth, Cookies, Verification with pytest

# GET Request - Booking ID
### Request
# URL -> https://restful-booker.herokuapp.com/booking/1
# AUTH? - No
# Payload? - No
# Content-Type - or Header? - No
# Query Param? - No
# Path Param? - Yes - 1

### Response
# Body --> Verify - Assert --> Keys and Values
# Status Code --> Verify
# Time verification
# JSON Schema or XML Schema

import pytest
import allure
import requests

@allure.title("Test GET Booking By Id Request - RESTful Booker project # 1")
@allure.description("TC#1 -> Verify that GET Request with ID works")
@allure.tag("Regression", "p1", "smoke")
@allure.label("Tester", "Suresh")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_booking_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url, verify=False)
    print(responseData.json())
    assert responseData.status_code == 200

@allure.title("Test GET Booking By Id Request - RESTful Booker project # 1")
@allure.description("TC#2 -> Verify that GET Request with invalid Id")
@allure.tag("Regression", "p1", "smoke")
@allure.label("Tester", "Suresh")
@allure.testcase("TC#2")
@pytest.mark.smoke
def test_get_single_booking_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responseData = requests.get(url, verify=False)
    # print(responseData.json())
    print(responseData.text)
    assert responseData.status_code == 404

@allure.title("Test GET Booking By Id Request - RESTful Booker project # 1")
@allure.description("TC#3 -> Verify that GET Request with invalid Id")
@allure.tag("Regression", "p2")
@allure.label("Tester", "Suresh")
@allure.testcase("TC#3")
@pytest.mark.regression
def test_get_single_booking_by_id_negative2():
    url = "https://restful-booker.herokuapp.com/booking/2"
    responseData = requests.get(url, verify=False)
    # print(responseData.json())
    print(responseData.text)
    assert responseData.status_code == 404