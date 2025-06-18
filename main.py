import turtle
import pandas

screen = turtle.Screen()
image = "blank_img.gif"
screen.addshape(image)
turtle.shape(image)


csv_data = pandas.read_csv("50_states.csv")
all_state = csv_data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State",prompt="What's another state's name ?").title()
    
    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_state:
        guessed_states.append(answer_state)
        T = turtle.Turtle()
        T.hideturtle()
        T.penup()
        state_data = csv_data[csv_data.state == answer_state]
        T.goto(x=state_data.x.item(),y=state_data.y.item())
        T.write(state_data.state.item())


