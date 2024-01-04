import turtle 

class user(turtle):
    def __init__(self):
        screen = turtle.Screen()
        super().__init__()
        answer_state = screen.textinput(title="Guess the State", prompt="What is another state name")
    
    def get_mouse_click_coor(self,x,y):
            print(x,y)
    
        