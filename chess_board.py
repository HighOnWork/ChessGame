import tkinter as tk

class chess_board:
    def __init__(self):
        self.window_maker = tk.Tk()
        self.canvas = tk.Canvas(height=1000, width=1000)
    def create_board(self):
        self.window_maker.minsize(600, 600)
        self.canvas.config(bg="brown")
    def lining(self):
        x1 = 1
        Y1 = 0
        x2 = 1
        Y2 = 1000
        for i in range(8):
            self.canvas.create_line(x1, Y1, x2, Y2)
            x1 = round(x1 * 66.67)
            x2 = round(x2 * 66.67)

    def config(self):
        self.canvas.grid(column=0, row=0)
        self.window_maker.mainloop()