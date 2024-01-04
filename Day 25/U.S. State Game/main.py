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
def get_mouse_click_coor(x,y):
    print(x,y)


guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 State Correct", prompt="What is another state name").title()
    
    if answer_state == "Exit":
        missing_state = []
        for state in state_li:
            if state not in guessed_states:
                missing_state.append(state)
        print(missing_state)
        break
    
    if answer_state in state_li:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
    



turtle.onscreenclick(get_mouse_click_coor)

