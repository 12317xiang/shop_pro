#注册
#1.正常注册，2.注册完了登录，如果登录失败则进行注册，3.注册不能使用已经注册过的用户名
type_one = {1:'注册',2:"登录",3:"退出",4:"修改用户信息"} #类型      
UserList = [['admin','123']]
#注册
def register():
    name = input("请输入用户名：")
    pas = input("请输入密码：")
    c_pas = input("请再次输入密码")
    for count in UserList:
        if name in count[0]:
            print("用户名已存在，注册失败，请重新注册")
            register()
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
                    login()      
            
                    
# 登录
def login():
    print(UserList)
    name = input("请输入登录用户名：")
    pas = input("请输入登录密码：")
    for count in UserList:
        if count[0] == name and count[1] == pas:
            print("登录成功")
            Xiugai_User([name,pas])
            break
        else:
            print("登录失败，请重新登录！")
            login()
            
#修改用户信息
#1.首先需要登录，修改用户名和修改密码只能单个存在，
def Xiugai_User(users):
    text = input("请选择你需要修改的用户信息! （1修改用户名   2.修改密码）")
    for count in UserList:
        if text == "1":
            # text_old_name = input("请输入原用户名：")
            # if len(text_old_name) == 0:
            #     print("原用户名不能为空")
            # elif text_old_name == count[0]:
            text_new_name = input("请输入新用户名：")
            if len(text_new_name) != 0:
                print('用户名修改成功')
                UserList.append([text_new_name,users[1]])
                print("__________：",text_new_name)
                print(UserList)
                break
            else:
                print("新用户名不能为空")
        elif text == "2":
            text_old_pas = input("请输入原密码：")
            if text_old_pas != users[1]:
                print("输入的密码与原密码不匹配")
            elif text_old_pas == count[1]:
                text_new_pas = input("请输入新密码：")
                c_text_new_pas = input("请再次确认新密码：")
                if len(text_new_pas) != 0 and text_new_pas == c_text_new_pas:
                    print('密码修改成功,请重新登录')
                    UserList.append([users[0],text_new_pas])
                    login()
                elif text_new_pas != c_text_new_pas:
                    print("两次输入的密码不一致")
                else:
                    print("新密码输入有误")
    
#判断选择的类型
def xuanze():
    aa = input("请选择你需要操作的选项！(1:注册   2:登录   3:退出   4:修改用户信息)  ：")
    if aa == '1':
        print("oo1")
        register()
        return
    elif aa == '2':
        login()
    elif aa == '3':
        print("退出登录成功,欢迎回到登录页面")
        shouye = input("请选择你需要操作的选项！(1:注册   2:登录)  ：")
        if shouye == '1':
            register()
        elif shouye == '2':
            login()
    elif aa == '4':
        Xiugai_User()
    else:
        print("输入的类型有误")
xuanze()

