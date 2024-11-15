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
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.first.x, self.second.y, self.second.x, self.first.y, fill=fill_color, width=2)
