
import unittest

from day07.ihrm_system.case.TestIHRMEmploye import TestEmployee
from day07.ihrm_system.case.TestIHRMUser import TestUser

suite=unittest.TestSuite()
suite.addTest( TestUser("test_login_success"))
suite.addTest(TestEmployee("test_emp_add"))
suite.addTest(TestEmployee("test_emp_update"))
suite.addTest(TestEmployee("test_emp_get"))
suite.addTest(TestEmployee("test_emp_delete"))


runner=unittest.TextTestRunner()
runner.run(suite)