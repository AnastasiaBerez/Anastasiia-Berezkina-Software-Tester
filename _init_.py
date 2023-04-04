from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.SignIn.locator import Locators
from pages.SignIn.element import Element, InputElement, ButtoElement


class User:
    def __init__(self, email_login, password): #sign_in_button, #fogot_password):
        self.email_login = email_login
        self.password = password
        #self.sign_in_button = sign_in_button
        #self.fogot_password = fogot_password


class SignIn():
    path = "/user/signin"
    def __init__(self, browser):
        self.email_login = InputElement(driver=browser.get_driver(), locator=Locators.email_login_locator)
        self.password = InputElement(driver=browser.get_driver(), locator=Locators.password_locator)
        self.sign_in_button = ButtoElement(driver=browser.get_driver(), locator=Locators.sign_in_button_locator)

    def signin(self, user: User):
        self.email_login.enter_text(user.email_login)
        self.password.enter_text(user.password)
        self.sign_in_button.click_element()


