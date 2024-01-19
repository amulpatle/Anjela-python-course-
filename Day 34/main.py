import requests

parameters = {
    "amount":10,
    # "category":"",
    # "difficulty":"",
    "type":"boolean",
}

# response = requests.get(url="https://opentdb.com/api.php?",params=parameters)
# response.raise_for_status()
# data = response.json()

# listdata = data["results"]
# # print(listdata[0])
# distdata = listdata[0]
# questiondata = distdata["question"]
# print(questiondata)

# print(data["results"])


def police_check(age:int)->bool: # THis is called type check in python '->' this indicate this function return type in fucntion calling 
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


police_check(12)