from tkinter import Tk, BOTH, Canvas
from graphics import *

class Cell:
    def __init__(self, win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        # Calculate the midpoint of the current cell
        mid_x1 = (self._x1 + self._x2) / 2
        mid_y1 = (self._y1 + self._y2) / 2
        
        # Calculate the midpoint of the target cell
        mid_x2 = (to_cell._x1 + to_cell._x2) / 2
        mid_y2 = (to_cell._y1 + to_cell._y2) / 2
        
        # Determine the color based on the undo parameter
        color = "red" if not undo else "gray"
        
        # Draw the line between the midpoints
        line = Line(Point(mid_x1, mid_y1), Point(mid_x2, mid_y2))
        self._win.draw_line(line, fill_color=color)