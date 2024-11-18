from tkinter import Tk, BOTH, Canvas

class Window ():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Generator")
        self.__canvas = Canvas(self.__root,bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("window closed...")
    
    def close(self):
        self.running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, first_point, second_point):
        self.first = first_point
        self.second = second_point
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.first.x, self.second.y, self.second.x, self.first.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
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
        color = "red" if undo else "green"
        
        # Draw the line between the midpoints
        line = Line(Point(mid_x1, mid_y1), Point(mid_x2, mid_y2))
        self._win.draw_line(line, fill_color=color)