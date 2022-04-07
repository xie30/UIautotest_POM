
import unittest,time
import sys
from selenium import webdriver
from pages.login_page import login

# reload(sys)
# sys.setdefaultencoding("utf-8")


# 百度搜索测试
class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testLogin(self):
        driver = self.driver
        #登录的链接
        url = ""
        # email and passw
        email = ''
        passw = ''
        log_in = login(driver, url)
        #打开登录页面
        log_in.goto()
        driver.implicitly_wait(10)
        driver.maximize_window()
        #输入账号密码
        log_in.input_user(email, passw)

        #点击登录
        log_in.click_log_btn()
        time.sleep(10)
        driver.save_screenshot('登录完成截图.png')
        #验证登录成功class="MuiList-root MuiList-padding
        driver.implicitly_wait(10)
        self.assertIsNotNone(log_in.get_robot_list())
        # driver.implicitly_wait(10)
        # time.sleep(10)

        # # 验证标题
        # self.assertEqual(search_Page.get_title(), assert_title)

    def tearDown(self):
        self.driver.quit()
        # pass

if __name__ == "main":
    TestLoginPage()
