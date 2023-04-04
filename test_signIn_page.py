from pages.SignIn._init_ import SignIn, User
from browser import Browser
import pytest
import time


@pytest.fixture()
def user_test():
    return User(email_login="Test@test.ru", password ="qwerty123")


@pytest.fixture()
def browser():
    return Browser()

class TestSignInPage:

    def test_signIn(self,browser,user_test):
        browser.go_to_site(SignIn.path)
        browser.driver.implicitly_wait(10)
        page = SignIn(browser)
        page.signin(user_test)
        time.sleep(5)
