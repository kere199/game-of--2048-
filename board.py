from turtle import Turtle,Screen
class Board:
    def __init__(self):
     self.t = Turtle()
     self.t.hideturtle()
     self.t.penup()
     self.t.goto(-100,300)
     self.t.setheading(0)
     self.tiles = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]


    def draw_tiles(self):
       for row  in self.tiles:
          for num in row:
             self.t.write(num)
             self.t.forward(50) 
          self.t.goto(-100, self.t.ycor() - 50)