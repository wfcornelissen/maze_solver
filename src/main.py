from window import *

def main():
    win = Window(800,600)
    c = Cell(win)
    c.west = False
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.east = False
    c.draw(125, 125, 200, 200)

    c = Cell(win)
    c.south = False
    c.draw(225, 225, 250, 250)

    c = Cell(win)
    c.north = False
    c.draw(300, 300, 500, 500)

    win.wait_for_close()

main()