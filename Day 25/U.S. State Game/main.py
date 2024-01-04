import turtle 

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "/home/amul/Documents/anjela python/Day 25/U.S. State Game/blank_states_img.gif"
screen.bgpic(image)

answer_state = screen.textinput(title="Guess the State", prompt="What is another state name")

def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
