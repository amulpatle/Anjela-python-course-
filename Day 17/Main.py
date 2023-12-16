class User:
    def __init__(self,username,id) :
        print("This is car object")
        self.username = username
        self.user_id = id
        self.followers = 0
        self.following = 0
    def follow(self,user):
        user.followers +=1
        self.following +=1

user1 = User("amul",1002)
print(user1.username)

user2 = User("Mohit",112)

user1.follow(user2)

print(user1.following)
print(user1.followers)
print(user2.following)
print(user2.followers)