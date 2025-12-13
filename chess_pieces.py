import tkinter as tk
from PIL import Image, ImageTk

global img_ref 

class ChessPieces:
    def __init__(self, windowMaker, canvas):
        self.window_maker = windowMaker
        self.canvas = canvas
        self.new_width = 75
        self.new_height = 75
        self.center_x = 63
        self.center_y = 190
    def black_pawn(self):
        global img_ref
        unconvertedImage = Image.open(r"C:\Users\HighO\OneDrive\Documents\GitHub\ChessEngine\BlackPawn.png")
        resized_image = unconvertedImage.resize((self.new_width, self.new_height), Image.Resampling.LANCZOS)
        img_ref = ImageTk.PhotoImage(resized_image) 
        new_x_for_each_pawn = self.center_x
        for _ in range(8):
            self.canvas.create_image(new_x_for_each_pawn, self.center_y, image=img_ref)
            new_x_for_each_pawn += 125
        