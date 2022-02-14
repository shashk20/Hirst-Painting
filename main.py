# import colorgram
import turtle as t
import random
t.colormode(255)
# colors = colorgram.extract("hirst painting.jpg", 15)
color_list = [(250, 251, 247), (199, 168, 94), (227, 239, 232), (129, 179, 191), (163, 58, 78), (234, 221, 121),
              (49, 113, 167), (241, 217, 222), (104, 87, 83), (143, 187, 119), (239, 245, 249), (216, 151, 171),
              (67, 125, 76), (94, 124, 180), (85, 165, 94)]
random.choice(color_list)
tim=t.Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.penup()
tim.setpos(-150,-180)
for i in range(10):
    for j in range(10):
        tim.dot(20,random.choice(color_list))
        tim.penup()
        tim.forward(50)
    tim.goto(-150,-180+50*(i+1))



screen=t.Screen()
screen.exitonclick()