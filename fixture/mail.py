class MailHelper:

    def __init__(self, app):
        self.app = app

    def send(self, mail):
        driver = self.app.driver
        # open create mail
        driver.find_element_by_xpath(
            "//div[@id='app-canvas']/div/div/div/div/div[2]/span/div/div/div/div/div/div/div/div/a/span/span").click()
        # fill To field
        driver.find_element_by_xpath("(//input[@value=''])[2]").click()
        driver.find_element_by_xpath("(//input[@value=''])[2]").clear()
        driver.find_element_by_xpath("(//input[@value=''])[2]").send_keys(mail.address)
        # fill Subject field
        driver.find_element_by_name("Subject").click()
        driver.find_element_by_name("Subject").clear()
        driver.find_element_by_name("Subject").send_keys(mail.subject)
        # send mail
        driver.find_element_by_xpath("//div[2]/div/span/span/span").click()
        driver.find_element_by_xpath("//div[16]/div/div/div[2]/button/span").click()

    def delete(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//div[@id='app-canvas']/div/div/div/div/div[2]/span/div[2]/div/div/div/div/div/div/div/div/div/a/div[4]/div/div[3]/span/span").click()
        driver.find_element_by_xpath("//div[@id='app-canvas']/div/div/div/div/div/span/div[2]/table/tbody/tr/td/div/div/span/span/span[2]").click()