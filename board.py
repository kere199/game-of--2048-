from turtle import Turtle,Screen
import random
class Board:
    def __init__(self):
     self.t = Turtle()
     self.t.hideturtle()
     self.t.penup()
     self.t.setheading(0)
     self.tiles = [[0,0,0,0], [0,2,0,0], [0,0,0,0], [0,0,0,0]]


    def draw_tiles(self):
       self.t.clear()
       self.t.goto(-100,300)
       for row  in self.tiles:
          for num in row:
             self.t.write(num)
             self.t.forward(50) 
          self.t.goto(-100, self.t.ycor() - 50)



    def move_left(self):
        for row in range(4):
            for col in range(1, 4):
                if self.tiles[row][col] != 0:
                    x = col
                    while x > 0 and self.tiles[row][x - 1] == 0:
                        self.tiles[row][x - 1] = self.tiles[row][x]
                        self.tiles[row][x] = 0
                        x -= 1
                    if x > 0 and self.tiles[row][x - 1] == self.tiles[row][x]:
                        self.tiles[row][x - 1] += self.tiles[row][x]
                        self.tiles[row][x] = 0

        self.create_random_2()
        self.draw_tiles()


    def move_right(self):
        for row in range(4):
            for col in range(2, -1, -1):
                if self.tiles[row][col] != 0:
                    x = col
                    while x < 3 and self.tiles[row][x + 1] == 0:
                        self.tiles[row][x + 1] = self.tiles[row][x]
                        self.tiles[row][x] = 0
                        x += 1
                    if x < 3 and self.tiles[row][x + 1] == self.tiles[row][x]:
                        self.tiles[row][x + 1] += self.tiles[row][x]
                        self.tiles[row][x] = 0
        self.create_random_2()
        self.draw_tiles()


    def move_up(self):
        for col in range(4):
            for row in range(1, 4):
                if self.tiles[row][col] != 0:
                    y = row
                    while y > 0 and self.tiles[y - 1][col] == 0:
                        self.tiles[y - 1][col] = self.tiles[y][col]
                        self.tiles[y][col] = 0
                        y -= 1
                    if y > 0 and self.tiles[y - 1][col] == self.tiles[y][col]:
                        self.tiles[y - 1][col] += self.tiles[y][col]
                        self.tiles[y][col] = 0
        self.create_random_2()
        self.draw_tiles()

    def move_down(self):
        for col in range(4):
            for row in range(2, -1, -1):
                if self.tiles[row][col] != 0:
                    y = row
                    while y < 3 and self.tiles[y + 1][col] == 0:
                        self.tiles[y + 1][col] = self.tiles[y][col]
                        self.tiles[y][col] = 0
                        y += 1
                    if y < 3 and self.tiles[y + 1][col] == self.tiles[y][col]:
                        self.tiles[y + 1][col] += self.tiles[y][col]
                        self.tiles[y][col] = 0
        self.create_random_2()
        self.draw_tiles()

    
    def empty_spaces(self):
        empty_spaces = []
        for x in range(4):
            for y in range(4):
                if self.tiles[x][y] == 0:
                    empty_spaces.append((x,y))
        return empty_spaces




    def create_random_2(self):
        empties = self.empty_spaces()
        i = random.randint(0,len(empties)-1)
        row = empties[i][0]
        col = empties[i][1]
        self.tiles[row][col] = 2
        self.draw_tiles()











                   
       
      