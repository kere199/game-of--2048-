from turtle import Turtle,Screen
import random
class Board:
    def __init__(self):
     self.t = Turtle()
     self.t.hideturtle()
     self.t.penup()
     self.t.setheading(0)
     self.tiles = [[0,0,0,0], [0,2,2,2], [0,0,2,0], [0,0,0,0]]


    def draw_tiles(self):
       self.t.clear()
       self.t.goto(-100,300)
       for row  in self.tiles:
          for num in row:
             self.t.write(num)
             self.t.forward(50) 
          self.t.goto(-100, self.t.ycor() - 50)


    def move_right(self):
        for row in range(4):
            for col in range(0,3):
                if self.tiles[row][col] != 0:
                    x = col
                    while x < 3 and self.tiles[row][x + 1] == 0:
                        self.tiles[row][x + 1] = self.tiles[row][x]
                        self.tiles[row][x] = 0
                        x += 1
                    if x < 3 and self.tiles[row][x + 1] == self.tiles[row][x]:
                        self.tiles[row][x + 1] += self.tiles[row][x]
                        self.tiles[row][x] = 0
        for row in range(4):
            for col in range(3,0,-1):
                if self.tiles[row][col] != 0:
                    x = col
                    if  x < 3 and self.tiles[row][x + 1] == 0:
                        self.tiles[row][x + 1] = self.tiles[row][x]
                        self.tiles[row][x] = 0
        
        self.draw_tiles()








                   
       
      