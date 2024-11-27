import turtle
from turtle import Turtle

import pandas
data = pandas.read_csv("28_states.csv")
screen = turtle.Screen()

screen.title("Indian states guessing game")
image = "india.gif"

screen.addshape(image)
turtle.shape(image)

states = data.state.to_list()
guessed =[]
missing = []
while len(guessed)<50:
    answer = screen.textinput(f"{len(guessed)}/28 guessed correctly", "Whats ur guess").title()
    if answer == "Exit":
        for state in states:
            if state not in guessed:
                missing.append(state)
        break
    if answer in states:
        guessed.append(answer)
        tim = Turtle()
        tim.hideturtle()
        tim.penup()
        sdata = data[data.state == answer]
        tim.goto(sdata.x.item() , sdata.y.item())
        tim.write(answer,move= True, align= "center",font= ("Aptos",8,"normal") )

datas = pandas.DataFrame(missing)
datas.to_csv("Misses.csv")

screen.exitonclick()