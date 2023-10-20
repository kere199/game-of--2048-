from turtle import Turtle,Screen
from board import Board
screen = Screen()
screen.tracer(0)
board = Board()
board.draw_tiles()


screen.listen()
screen.onkeypress(fun=board.move_right, key = "Right")

screen.update()


screen.exitonclick()