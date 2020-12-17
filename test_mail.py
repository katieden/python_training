# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class M4(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_m4(self):
        driver = self.driver
        driver.get("https://mail.ru/?from=logout")
        driver.find_element_by_name("login").click()
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys("katieden")
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("rjnktnrf.12ml")
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_xpath(
            "//div[@id='app-canvas']/div/div/div/div/div[2]/span/div/div/div/div/div/div/div/div/a/span/span").click()
        driver.find_element_by_xpath("(//input[@value=''])[2]").click()
        driver.find_element_by_xpath("(//input[@value=''])[2]").clear()
        driver.find_element_by_xpath("(//input[@value=''])[2]").send_keys("katieden7@gmail.com")
        driver.find_element_by_name("Subject").click()
        driver.find_element_by_name("Subject").clear()
        driver.find_element_by_name("Subject").send_keys("hello2")
        driver.find_element_by_xpath("//div[2]/div/span/span/span").click()
        driver.find_element_by_xpath("//div[16]/div/div/div[2]/button/span").click()
        driver.find_element_by_id("PH_logoutLink").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
