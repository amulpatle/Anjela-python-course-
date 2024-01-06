student_dict = {
    "student" : ["Amul","Saurav","Aditya","Pratik"],
    "Score":[65,33,79,90]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key,value) in student_data_frame.items():
#     print(key)
    
# Loop through rows of a data frame

for (index,row)  in student_data_frame.iterrows():
    print(row)