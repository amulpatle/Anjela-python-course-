import requests

parameters = {
    "amount":10,
    # "category":"",
    # "difficulty":"",
    "type":"boolean",
}

response = requests.get(url="https://opentdb.com/api.php?",params=parameters)
response.raise_for_status()
data = response.json()

listdata = data["results"]
# print(listdata[0])
distdata = listdata[0]
questiondata = distdata["question"]
print(questiondata)

# print(data["results"])