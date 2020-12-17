from selenium import webdriver


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def logout(self):
        driver = self.driver
        driver.find_element_by_id("PH_logoutLink").click()

    def send_mail(self, mail):
        driver = self.driver
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

    def login(self, username, password):
        driver = self.driver
        self.open_url()
        driver.find_element_by_name("login").click()
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys(username)
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()

    def open_url(self):
        driver = self.driver
        driver.get("https://mail.ru/?from=logout")

    def destroy(self):
        self.driver.quit()

