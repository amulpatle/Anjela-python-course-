
#  if we write this way we don't need to close file menualy
# with  open("/home/amul/Documents/anjela python/Day 24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)
    # file.close()
    
# file = open("/home/amul/Documents/anjela python/Day 24/my_file.txt") 
# contents = file.read()
# print(contents)
# file.close()

with open("/home/amul/Documents/anjela python/Day 24/my_file.txt","w") as file:
    file.write("hey,this is new one")

with open("/home/amul/Documents/anjela python/Day 24/my_file.txt", mode="a") as file:
    file.write("My Name Is Amul Patle")