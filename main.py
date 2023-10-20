from turtle import Turtle,Screen
from board import Board
screen = Screen()
screen.tracer(0)
board = Board()
board.draw_tiles()


screen.listen()
screen.onkeypress(fun=board.move_right, key = "Right")
screen.onkeypress(fun= board.move_left, key = 'Left' )
screen.onkeypress(fun= board.move_up, key = 'Up' )
screen.onkeypress(fun= board.move_down, key = 'Down' )

screen.update()


screen.exitonclick()