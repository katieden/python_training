class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        driver = self.app.driver
        self.app.open_url()
        driver.find_element_by_name("login").click()
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys(username)
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_id("PH_logoutLink").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
        else:
            self.logout()
        self.login(username, password)

    def is_logged_in(self):
        driver = self.app.driver
        return len(driver.find_element_by_id("PH_logoutLink")) > 0
# krfl;re2342
    def is_logged_in_as(self, username):
        driver = self.app.driver
        return driver.find_element_by_id("PH_user-email").text == username+"@mail.ru"