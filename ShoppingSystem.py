#注册
from User import User
from UserList import UserList
class ShoopingSystem:

    @staticmethod
    def register():
        userName = input("请输入用户名：")
        password = input("请输入密码：")
        C_password = input("请在此输入密码：")
        userList = UserList()
        if len(userName) == 0 or len(password) == 0 or password != C_password:
            print("注册失败")
        else:
            newUser = User(userName, password)
            searchUser = userList.getUserByUserName(newUser.userName)
            if searchUser:
                print("用户名存在")
            else:
                userList.append(newUser)
                print("注册成功，去登录吧") 
                print(newUser) 

ShoopingSystem.register()