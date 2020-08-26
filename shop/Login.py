#注册
#1.正常注册，2.注册完了登录，如果登录失败则进行注册，3.注册不能使用已经注册过的用户名
type_one = {1:'注册',2:"登录",3:"退出"}       
UserList = []
aa = input("请输入你的选择：")
class Users:
    if aa == 1:
        def register(self):
            name = input("请输入用户名：")
            pas = input("请输入密码：")
            c_pas = input("请再次输入密码")
            if len(name) != 0 and len(pas) != 0 and c_pas == pas:
                print("注册成功，去登录吧")
                UserList.append([name,pas])
            else:
                if len(name) == 0 or len(pas) == 0 or c_pas != pas:
                        print("注册失败")
                else:       
                    for count in UserList:
                        if name in count:
                            print("用户名已存在，无法进行重新注册")
    # 登录
    elif aa == 2:
        def login(self):
            print(UserList)
            name = input("请输入登录用户名：")
            pas = input("请输入登录密码：")
            for count in UserList:
                if count[0] == name and count[1] == pas:
                    print("登录成功")
                    break
                else:
                    print("登录失败")
    elif aa == 3:
        print("退出登录成功")