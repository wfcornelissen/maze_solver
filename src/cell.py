from tkinter import Tk, BOTH, Canvas
from graphics import *

class Cell:
    def __init__(self, win, x1,y1,x2,y2):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
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