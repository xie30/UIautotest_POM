import unittest
import sys

from testcase.test_log import TestLoginPage
import HTMLTestRunner
# reload(sys)
# sys.setdefaultencoding("utf-8")

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(TestLoginPage('testLogin'))

    # 定义报告输出路径
    htmlPath = u"page_demo_Report.html"
    with open(htmlPath, "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='自动化测试报告', description='详细测试用例结果', verbosity=0)
        runner.run(testunit)
        # unittest.main()
