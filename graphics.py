from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        # Create the root window
        self.root = Tk()
        self.root.title("Maze Solver")

        # Create the canvas
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)

        # Window state
        self.running = False

        # Connect the window's close button (X) to the self.close method
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        # Forces Tkinter to update the window and any changes on the canvas
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        
    def close(self):
        self.running = False

def main():
    win = Window(800, 600)  # You can change the width and height as needed
    win.wait_for_close()

if __name__ == "__main__":
    main()