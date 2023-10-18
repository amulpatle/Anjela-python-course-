traveling_log = {"mp":["balaghat","Bhopal, Indore"]
                 ,"Gujrat":{"not_visited" :["surat","patna"],"total_visited":12}}

# for cities in traveling_log:
#     print(traveling_log[cities])


planning_to_travel = [

    {"mp":["ujjain","Indore","omkaleshwar","jabalpur"],
     "total_number_visited":12
    },
    {
        "tamilnadu":["tiruannatpuram","kanyaKumari"],
        "total_number_visited":5
    }
]


def add_new_data(name,visited,times):
    new_country = {}
    new_country["country"] = name
    new_country["visited"] = visited
    new_country["times"] = times
    
    planning_to_travel.append(new_country)


add_new_data("mashrashtra","mumbai",2)
for i in  planning_to_travel:
    print(i)