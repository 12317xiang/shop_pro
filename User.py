class User:
    def __init__(self,userName,password):
        self.userName = userName
        self.password = password
    def setId(self, id):
        self.id = id

list1 = [[User([1,2], [3,4])]]
print(list1[0][0].password[1])

print(123 in [123])
