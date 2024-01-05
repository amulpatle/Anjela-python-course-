number = [1,2,3]
new_number = [n+1 for n in number]
print(new_number)

name = "Amul"

new_name = [letter for letter in name]
print(new_name)

names = ["Amul","Saurav","Pratik","Ashish","Ankit","Nikki","Mansi"]

name_list = [name.upper() for name in names if len(name) <= 5]
print(name_list)