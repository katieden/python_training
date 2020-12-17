# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class SortTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_sort(self):
        driver = self.driver
        self.open_url(driver)
        self.login(driver, "admin", "Demo!1234")
        self.sorting(driver)

    def sorting(self, driver):
        driver.find_element_by_xpath(
            "//body[@id='main']/app-root/app-main/div/div[2]/app-dashboard/div/div[6]/app-card/div").click()
        driver.find_element_by_xpath("//span[2]").click()
        driver.find_element_by_xpath("//li/a/span").click()
        driver.find_element_by_xpath("//th/span").click()
        driver.find_element_by_xpath("//th/span").click()
        #for i in range(1, 3):
            #driver.find_element_by_xpath("//th[i]/span").click()
           # driver.find_element_by_xpath("//th[i]/span").click()

    / html / body / app - root / app - equipment / div / div / app - equipment - list / app - data - table / div / app - m - table / \
      div[1] / table / thead / tr / th[1]

    / html / body / app - root / app - equipment / div / div / app - equipment - list / app - data - table / div / app - m - table / \
      div[1] / table / thead / tr / th[2]

    / html / body / app - root / app - equipment / div / div / app - equipment - list / app - data - table / div / app - m - table / \
      div[1] / table / thead / tr / th[3]

    def login(self, driver, username, password):
        driver.find_element_by_xpath("//input[@type='text']").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys(username)
        driver.find_element_by_xpath("//body[@id='main']/app-root/app-auth/div/div").click()
        driver.find_element_by_xpath("(//input[@type='password'])[2]").click()
        driver.find_element_by_xpath("(//input[@type='password'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys(password)
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys(Keys.ENTER)

    def open_url(self, driver):
        driver.get("https://demo.core.heineken.com/CAWA/signin")

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
