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
    print("JSON Response : \n", responseData.json())
    print("Text Response : \n", responseData.text)
    print("Header Information : ", responseData.headers)
    print("Cookies : ", responseData.cookies)
    assert responseData.status_code == 200



