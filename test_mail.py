# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class test_mail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []

    def test_m4(self):
        driver = self.driver
        self.open_url(driver)
        self.login(driver)
        self.send_mail(driver)
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_id("PH_logoutLink").click()

    def send_mail(self, driver):
        # open create mail
        driver.find_element_by_xpath(
            "//div[@id='app-canvas']/div/div/div/div/div[2]/span/div/div/div/div/div/div/div/div/a/span/span").click()
        # fill To field
        driver.find_element_by_xpath("(//input[@value=''])[2]").click()
        driver.find_element_by_xpath("(//input[@value=''])[2]").clear()
        driver.find_element_by_xpath("(//input[@value=''])[2]").send_keys("katieden7@gmail.com")
        # fill Subject field
        driver.find_element_by_name("Subject").click()
        driver.find_element_by_name("Subject").clear()
        driver.find_element_by_name("Subject").send_keys("hello2")
        # send mail
        driver.find_element_by_xpath("//div[2]/div/span/span/span").click()
        driver.find_element_by_xpath("//div[16]/div/div/div[2]/button/span").click()

    def login(self, driver):
        driver.find_element_by_name("login").click()
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys("katieden")
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("rjnktnrf.12ml")
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()

    def open_url(self, driver):
        driver.get("https://mail.ru/?from=logout")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
