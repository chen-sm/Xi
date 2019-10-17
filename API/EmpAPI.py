from day07.ihrm_system import app


class EmpCRUD:

    # 函数1：增
    def add(self,session,username,mobile,workNumber):
        myAddEmp={
            "username":username,
            "mobile":mobile,
            "workNumber":workNumber
        }
        return session.post(app.BASE_PATH+"user",
                            json=myAddEmp,
                            headers={"Authorization":"Bearer "+app.TOKEN})

    # 函数2：改
    def update(self,session,userId,username):
        return session.put(app.BASE_PATH+"user/"+userId,
                           json={"username":username},
                           headers={"Authorization":"Bearer "+app.TOKEN})
        pass

    # 函数3：查
    def get(self,session,userId):
        return session.get(app.BASE_PATH+"user/"+userId,
                           headers={"Authorization":"Bearer "+app.TOKEN})

    # 函数4：删
    def delete(self,session,userId):
        return session.delete(app.BASE_PATH+"user/"+userId,
                              headers={"Authorization":"Bearer "+app.TOKEN})