import turtle 
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "/home/amul/Documents/anjela python/Day 25/U.S. State Game/blank_states_img.gif"
screen.bgpic(image)

# with open("/home/amul/Documents/anjela python/Day 25/U.S. State Game/50_states.csv") as state_data:
#     data = state_data["state"]
    
# print(data)

data = pandas.read_csv("/home/amul/Documents/anjela python/Day 25/U.S. State Game/50_states.csv")
state_li = data.state.to_list()
# print(state)


answer_state = screen.textinput(title="Guess the State", prompt="What is another state name")

def get_mouse_click_coor(x,y):
    print(x,y)

if answer_state in state_li:
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x),int(state_data.y))
    t.write(answer_state)
    



turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
