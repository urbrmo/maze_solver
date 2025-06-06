from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        # Create the root window
        self.__root = Tk()
        self.__root.title("Maze Solver")

        # Create the canvas
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)

        # Window state
        self.__running = False

        # Connect the window's close button (X) to the self.close method
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        # Forces Tkinter to update the window and any changes on the canvas
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

        
    def close(self):
        self.__running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color = "black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
