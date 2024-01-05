# dictionary comprehension = create dictionaries using an expression
# can replace for loops and certain lambda functions

# dictionary = {key: expression for (key,value) in iterable}


# dictionary = {key: expression for (key,value) in iterable if conditional}

# dictionary = {key: (if/else) for (key,value) in iterable}


# dictionary = {key: function(value) for (key,value) in iterable}

cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

cities_in_c = {key: round((value-32)*(5/9)) for(key,value) in cities_in_F.items()}

print(cities_in_c)

weather = {'New York' : "snowing",
           'Boston' :"sunny",
           'Los Angeles':"sunny",
           'Chicago':"cloudy"
           }
sunny_weather = {key:value for(key,value) in weather.items() if value == "sunny"}

print(sunny_weather)

desc_cities = {key:("Warm" if value >= 40 else "Cold") for(key,value) in cities_in_F.items()}
print(desc_cities)

def check_temp(value):
    if value < 40:
        return "COLD"
    elif value < 40 and value > 55:
        return "CLOUDY"
    else:
        return "HOT"

desc_cities2 = {key: check_temp(value) for(key,value) in cities_in_F.items()}
print(desc_cities2)