#注册
#1.正常注册，2.注册完了登录，如果登录失败则进行注册，3.注册不能使用已经注册过的用户名
type_one = {1:'注册',2:"登录",3:"退出"} #类型      
UserList = []
#注册
def register():
    name = input("请输入用户名：")
    pas = input("请输入密码：")
    c_pas = input("请再次输入密码")
    if len(name) != 0 and len(pas) != 0 and c_pas == pas:
        print("注册成功，去登录吧")
        UserList.append([name,pas])
        login()
    else:
        if len(name) == 0 or len(pas) == 0 or c_pas != pas:
                print("注册失败,请重新注册")
                if len(name) != 0 and len(pas) != 0 and c_pas == pas:
                    print("注册成功，去登录吧")
                    UserList.append([name,pas])
        else:       
            for count in UserList:
                if name in count:
                    print("用户名已存在，无法进行重新注册")
# 登录
def login():
    print(UserList)
    name = input("请输入登录用户名：")
    pas = input("请输入登录密码：")
    for count in UserList:
        if count[0] == name and count[1] == pas:
            print("登录成功")
            break
        else:
            print("登录失败")
#修改用户信息


#判断选择的类型
def xuanze():
    aa = input("请选择你需要操作的选项！(1:注册   2:登录   3:退出   4:修改用户信息)  ：")
    if aa == '1':
        print("oo1")
        register()
        return
    elif aa == '2':
        login()
    elif aa == 3:
        print("退出登录成功")
    elif aa == 4:
        print("功能正在开发中…………")
    else:
        print("输入的类型有误")
xuanze()

