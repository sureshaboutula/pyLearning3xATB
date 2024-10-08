# Web Automation - Selenium
# Page - You are going to automate

class VWO_Login_page:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.password == "pass123":
            print("Allowed to enter")
        else:
            print("Not allowed")

amit = VWO_Login_page("amit@gmail.com", "123")
amit.login_confirm()

suresh = VWO_Login_page("sureshtest@gmail.com", "pass123")
suresh.login_confirm()

