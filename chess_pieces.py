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
        self.center_y = 74
    def black_pawn(self):
        global img_ref
        unconvertedImage = Image.open(r"C:\Users\HighO\OneDrive\Documents\GitHub\ChessEngine\BlackPawn.png")
        resized_image = unconvertedImage.resize((self.new_width, self.new_height), Image.Resampling.LANCZOS)
        img_ref = ImageTk.PhotoImage(resized_image) 
        for _ in range(7):
            self.canvas.create_image(self.center_x, self.center_y, image=img_ref)
        