from turtle import Turtle,Screen
import random
class Board:
    def __init__(self):
     self.t = Turtle()
     self.t.hideturtle()
     self.t.penup()
     self.t.setheading(0)
     self.tiles = [[1,2,3,4], [5,6,1024,7], [8,9,20,10], [11,12,13,0]]
     self.game_over = False
     self.color_dict = {
            2: "lightblue",
            4: "lightgreen",
            8: "lightpink",
            16: "lightyellow",
            32: "lightcoral",
            64: "lightsalmon",
            128: "lightseagreen",
            256: "lightblue",
            512: "lightgreen",
            1024: "lightpink",
            2048: "lightyellow"
        }



    def draw_tiles(self):
        self.t.clear()
        cell_size = 50

        for row in range(4):
            for col in range(4):
                num = self.tiles[row][col]
                color = self.color_dict.get(num, "lightgray") 
                self.t.goto(-175 + col * cell_size + cell_size / 2, 175 - row * cell_size - cell_size / 2)
                self.t.begin_fill()
                self.t.fillcolor(color)
                for _ in range(4):
                    self.t.forward(cell_size)
                    self.t.right(90)
                self.t.end_fill()
                self.t.goto(-125 + col * cell_size, 125 - row * cell_size - 10)  
                self.t.write(num, align="center", font=("Arial", 16, "normal"))




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


    def check_win(self):
        for j in range(4):
            for i in range(1, 4):
                if self.tiles[i][j] == 2048:
                    return True
        return False 
    
    def print_win(self):
        bob = Turtle()
        bob.hideturtle()
        bob.penup()
        bob.goto(0,240)
        bob.write("well done! You Won!", align="center", font=("Arial", 40, "normal")) 

    def no_moves(self):
        for i in range(4):
            for j in range(4):
                if self.tiles[i][j] == 0:
                    return False 
                if (i > 0 and self.tiles[i][j] == self.tiles[i - 1][j]) or \
                (i < 3 and self.tiles[i][j] == self.tiles[i + 1][j]) or \
                (j > 0 and self.tiles[i][j] == self.tiles[i][j - 1]) or \
                (j < 3 and self.tiles[i][j] == self.tiles[i][j + 1]):
                    return False
        return True



    def print_gameover(self):
        bob = Turtle()
        bob.hideturtle()
        bob.penup()
        bob.goto(0,240)
        bob.write("sorry you have lost!", align="center", font=("Arial", 40, "normal")) 







                   
       
      