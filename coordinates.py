import turtle
import pandas
screen = turtle.Screen()

screen.title("Indian states guessing game")
image = "india.gif"
x_coor=[]
y_coor =[]
screen.addshape(image)
turtle.shape(image)
def get_coor(x,y):
    x_coor.append(x)
    y_coor.append(y)
    print(x,y)

states = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana",
          "Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur",
          "Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu",
          "Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]

turtle.onscreenclick(get_coor)
turtle.mainloop()

dict = {
    "state":states, "x": x_coor, "y":y_coor
}
ty= pandas.DataFrame(dict)
ty.to_csv("28_states.csv")
print(len(x_coor))
print(len(y_coor))