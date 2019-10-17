
import unittest

# 创建测试类
import requests

from day07.ihrm_system import app
from day07.ihrm_system.API.EmpAPI import EmpCRUD


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.session=requests.Session()
        self.emp_obj=EmpCRUD()

    def tearDown(self):
        self.session.close()

    # 测试函数去1：增
    def test_emp_add(self):
        print("-" * 50+"添加员工" + "-" * 100)
        response=self.emp_obj.add(self.session,"lanzhanweiyin05","16709872349","2010001")
        print("新增成功响应结果",response.json())

        # 获取添加员工返回的id,赋值给全局变量.USER_ID，方便修改、查询、删除员工使用这个id
        user_add_id=response.json().get("data").get("id")
        print("打印获取添加员工返回的ID：", user_add_id)
        app.USER_ID=user_add_id


        # 测试函数去2：改
    def test_emp_update(self):
        print("-" * 50+"修改员工" + "-" * 100)
        response=self.emp_obj.update(self.session,app.USER_ID,"lanzhanweiyinAAD")
        print("修改后的响应体",response.json())
        self.assertEqual(True,response.json().get("success"))


    # 测试函数3：查
    def test_emp_get(self):
        print("-" * 50+'查询员工' + "-" * 100)
        response=self.emp_obj.get(self.session,app.USER_ID)

        self.assertEqual(True,response.json().get("success"))
        print("打印修改后员响应体",response.json())
        print("查询{}员工成功".format(app.USER_ID))


    # 测试函数4；删
    def test_emp_delete(self):
        print("-" * 50+"删除员工" + "-" * 100)
        response=self.emp_obj.delete(self.session,app.USER_ID)
        self.assertEqual(True,response.json().get("success"))
        print("删除添加{}员工成功".format(app.USER_ID))

