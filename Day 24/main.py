
#  if we write this way we don't need to close file menualy
with  open("/home/amul/Documents/anjela python/Day 24/my_file.txt") as file:
    contents = file.read()
    print(contents)
    # file.close()