from  fbchat import Client
from getpass import getpass
from fbchat.models import *

# username = str(input("Username: "))
# password = str(input("Password: "))
# print(username)
# print(password)

username = str(input("User:"))
password = str(input("pwd:"))

#client = fbchat.Client(username,getpass())
# no_of_friends = int(input("Number of friends: "))
# for i in range(no_of_friends):
#     name = str(input("Name: "))
#     friends = client.searchForUsers(name)
#     friend = friends[0]
#     msg = (input("Message: "))
#     sent = client.send(friend.uid,Message(text='👍', emoji_size=EmojiSize.LARGE))
#     #sent = client.send(friend.uid,msg)
#     if sent:
#         print("message sent successfully")

client = Client(username,password)

print('Own id: {}'.format(client.uid))


# if(friend):
#     print("found")
#     
client.send(Message(text='Good luck 👍'), thread_id=client.uid, thread_type=ThreadType.USER)

#users = client.fetchAllUsers()

#print("users' IDs: {}".format(user.uid for user in users))
#print("users' names: {}".format(user.name for user in users))

client.logout()


