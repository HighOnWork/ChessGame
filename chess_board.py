import tkinter as tk

class chess_board:
    def __init__(self):
        self.window_maker = tk.Tk()
        self.canvas = tk.Canvas(height=1000, width=1000)
    def create_board(self):
        self.window_maker.minsize(600, 600)
        self.window_maker.config(bg="brown")
    def lining(self):
        for i in range(8):
            self.canvas.create_line(0, 0, 0, 600)

    def config(self):
        self.canvas.grid(column=0, row=0)
        self.window_maker.mainloop()