import json
import unittest

# 创建测试类
import requests


# 编写Json解析数据
from parameterized import parameterized

from day07.ihrm_system import app
from day07.ihrm_system.API.UserAPI import UserLoign


def read_json():
    data=[]
    with open(app.File_Path+"/data/Login_data.json","r",encoding="utf-8") as f:
        for value in json.load(f).values():
            mobile=value.get("mobile")
            password=value.get("password")
            success=value.get("success")
            code=value.get("code")
            message=value.get("message")

            ele=(mobile,password,success,code,message)
            data.append(ele)
    # print(data)
    return data



class TestUser(unittest.TestCase):
    def setUp(self):
        self.session=requests.Session()
        self.user_obj=UserLoign()


    def tearDown(self):
        self.session.close()


    #测试函数：登录
    @parameterized.expand(read_json())
    def test_login(self,mobile,password,success,code,message):
        print("-"*100)
        print(mobile,password,success,code,message)
        response=self.user_obj.login_get(self.session,mobile,password)
        print(response.json())
        result=response.json()
        self.assertEqual(success,result.get("success"))
        self.assertEqual(code,result.get("code"))
        self.assertEqual(message,result.get("message"))

    #测试函数：只实现登录成功
    def test_login_success(self):
        print("-"*100)
        print("登录成功接口")
        response=self.user_obj.login_get(self.session,"13800000002","123456")
        result=response.json()
        print("登录成功的响应结果",result)
        self.assertEqual(True, result.get("success"))
        self.assertEqual(10000, result.get("code"))
        self.assertEqual("操作成功！", result.get("message"))
        token=result.get("data")
        print("登录成功后的token:",token)
        app.TOKEN=token
