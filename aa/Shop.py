# 注册
# UserList = []
# def register():
#     name = input("请输入用户名：")
#     pas = input("请输入密码:")
#     c_pas = input("请确认密码:")
    
#     if len(name) ==0 or len(pas) ==0 or pas != c_pas:
#         print("注册失败")
#     else:
#         for count in UserList:
#             if name in count:
#                 print("用户名已存在，请重新输入")
#                 break
#         UserList.append([name,pas])
#         print("注册成功")
#         print(UserList)
        
# register()

# def login():
#     name = input("请输入用户名：")
#     pas = input("请输入密码:")
#     for count in UserList:
#         if count[0] == name and count[1] == pas:
#             print("登录成功")
#         else:
#             print("登录失败")
#             register()
# login()

list1 = []
a = 123
b = "quw"
list1.append([a,b])
print(list1)
list1.append([])
    
    