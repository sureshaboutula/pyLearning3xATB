# Env File - .(dot.env)
# How do you store your password or credentials in the framework
# pip install python-dotenv

from dotenv import load_dotenv
import os

def test_update_request():
    load_dotenv()
    url = os.getenv("URL")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(url)
    print(username)
    print(password)
