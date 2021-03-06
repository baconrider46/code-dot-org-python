import sys
sys.path.append('../..')
import codestudio
z = codestudio.load('s1level86')

def draw_square():
    for count in range(4):
        z.move_forward(100)
        z.turn_right(90)

def draw_triangle():
    for count in range(3):
        z.move_forward(100)
        z.turn_right(120)

def draw_house():
    draw_square()
    z.move(100)
    z.right(30)
    draw_triangle()

draw_house()

z.check()
