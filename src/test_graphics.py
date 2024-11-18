from graphics import *

def test_line():
    win = Window(800, 600)

    w1 = Line(Point(100, 100), Point(125, 200))
    win.draw_line(w1)
    w2 = Line(Point(125, 200), Point(150, 150))
    win.draw_line(w2)
    w3 = Line(Point(150, 150), Point(175, 200))
    win.draw_line(w3)
    w4 = Line(Point(175, 200), Point(200, 100))
    win.draw_line(w4)
    
    win.wait_for_close()


def test_cell():
    win = Window(800, 600)
    cell = Cell(win)
    cell.draw(2, 2, 102, 102)
    win.wait_for_close()

test_cell()