import tkinter as tk

class chess_board:
    def __init__(self):
        self.window_maker = tk.Tk()
        self.canvas = tk.Canvas()
    def create_board(self):
        self.window_maker.minsize(600, 600)
        self.canvas.create_line(0, 0, 300, 300)
        self.window_maker.config(bg="brown")
    def config(self):
        self.canvas.grid(column=0, row=0)
        self.window_maker.mainloop()