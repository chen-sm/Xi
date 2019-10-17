import time
import unittest
from BeautifulReport import BeautifulReport
from case.TestIHRMEmploye import TestEmployee
from case.TestIHRMUser import TestUser

suite=unittest.TestSuite()
suite.addTest( TestUser("test_login_success"))
suite.addTest(TestEmployee("test_emp_add"))
suite.addTest(TestEmployee("test_emp_update"))
suite.addTest(TestEmployee("test_emp_get"))
suite.addTest(TestEmployee("test_emp_delete"))


# runner=unittest.TextTestRunner()
# runner.run(suite)
# bea_report="ihrm{}.html".format(time.strftime("%Y%m%d%H%M%S"))

BeautifulReport(suite).report(filename="bea_report.html",description="人力资源测试报告",log_path="./report_test/")