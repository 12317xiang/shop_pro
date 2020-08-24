#注册
UserList = []
def register():
    name = input("请输入用户名：")
    pas = input("请输入密码：")
    c_pas = input("请再次输入密码")
    if len(name) == 0 or len(pas) == 0 or c_pas != pas:
        print("注册失败，请确认输入的用户信息")
    else:
        UserList.append([name,pas])
        print("注册成功，去登录吧")
        return
        for count in UserList:
            if UserList[count] == name:
                print("用户名已存在，无法进行重新注册")
            else:
                register()
register()

#登录
def login():
    print(UserList)
    name = input("请输入登录用户名：")
    password = input("请输入登录密码：")
    if name in UserList and password == UserList[name]['pas']:
        print("登录成功")
    else: 
        print("登录失败")
login()