from selenium import webdriver
from fixture.session import SessionHelper
from fixture.mail import MailHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.mail = MailHelper(self)

    def open_url(self):
        driver = self.driver
        driver.get("https://mail.ru/?from=logout")

    def destroy(self):
        self.driver.quit()

