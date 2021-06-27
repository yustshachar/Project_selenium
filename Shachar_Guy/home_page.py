class home_page:
    def __init__(self, driver):
        self.driver=driver

    def category(self, name):
        return self.driver.find_element_by_id(f"{name}Img")

    def click_category(self, name):
        self.category(name).click()

    # def user_miniTitle_text(self):
    #     miniTitle = self.driver.find_elements_by_css_selector('[data-ng-show="userCookie.response"]')
    #     return miniTitle[0].text
    #     # return self.driver.find_element_by_xpath('//nav/ul/li/a/span[@data-ng-show="userCookie.response"][1]').text

    def nav_userIcon_click(self):
        self.driver.find_element_by_id('menuUser').click()

    def fill_username_field(self, input):
        self.driver.find_element_by_name('username').send_keys(input)

    def fill_password_field(self, input):
        self.driver.find_element_by_name('password').send_keys(input)

    def click_signIn_button(self):
        self.driver.find_element_by_id("sign_in_btnundefined").click()

