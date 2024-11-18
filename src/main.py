from graphics import *
from cell import *
from maze import *

def main():
    win = Window(800,600)
    maze = Maze(0, 0, 10, 10, 50, 50, win)
    
    win.wait_for_close()

main()