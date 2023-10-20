from turtle import Turtle,Screen
from board import Board
import turtle as t
import time
screen = Screen()
screen.tracer(0)
board = Board()
board.draw_tiles()




screen.listen()
screen.onkeypress(fun=board.move_right, key = "Right")
screen.onkeypress(fun= board.move_left, key = 'Left' )
screen.onkeypress(fun= board.move_up, key = 'Up' )
screen.onkeypress(fun= board.move_down, key = 'Down' )

game_over = False
while not game_over:
    screen.update()
    if board.check_win():
            board.print_win()
            screen.update()
            time.sleep(2)
            t.bye()
    if board.no_moves():
          board.print_gameover()
          screen.update()
          game_over = True
          time.sleep(2)
          t.bye()


# screen.update()


screen.exitonclick()
