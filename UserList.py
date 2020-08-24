class UserList():
    def __init__(self):
        self.userList = []
        self.count = 0
    def getUserByUserName(self, userName):
        for user in self.userList:
            if user.userName == userName:
                return user
    def append(self, user):
        user.setId(self.count)
        self.count += 1
        self.userList.append(user)
    