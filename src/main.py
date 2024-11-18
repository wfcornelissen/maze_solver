from graphics import *
from cell import *
from maze import *

def main():
    win = Window(800,600)
    c = Cell(win)
    c2 = Cell(win)
    c.draw(50, 50, 100, 100)
    c2.draw(125, 125, 200, 200)
    c.draw_move(c2)

    win.wait_for_close()

main()