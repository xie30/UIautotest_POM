

from pages.pagebase import PageBase
from selenium.webdriver.common.by import By

class login(PageBase):

    '''
    登录页面元素
    '''
    input_email =(By.ID, 'username')
    input_password = (By.ID, 'password')
    login_button = (By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/ul/li/form/div/div[3]/button')
    robot = (By.XPATH,'//*[@id="root"]/div[1]/header/div/ul/li[2]')


    def __init__(self, driver, baseurl):
        PageBase.__init__(self, driver, baseurl)

    def goto(self):
        print("打开登录登录页面: ",self.baseurl)
        self.driver.get(self.baseurl)

    def input_user(self, email, passw):
        self.input_text(email, self.input_email)
        self.input_text(passw, self.input_password)

    def click_log_btn(self):
        self.click(self.login_button)

    def get_robot_list(self):
        return self.robot_list(self.robot)

    def get_contract_list(self):
        return self.contract_list(self.contract)