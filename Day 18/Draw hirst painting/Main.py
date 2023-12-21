import colorgram
# print("hello")
colors = colorgram.extract('sweet_pic.jpeg', 6)
# print(colors)

rgb_color = []

for color in colors:
    rgb_color.append(color)

print(rgb_color)