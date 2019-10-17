"""
登录请求封装
"""
import logging

from day07.ihrm_system import app

# 封装登录请求
class UserLoign:

    # 登录请求
    def login_get(self,session,mobile,password):
        myData={
            "mobile":mobile,
            "password":password
        }
        logging.info("logging执行登录操作")
        return session.post(app.BASE_PATH+"login",
                            json=myData)
