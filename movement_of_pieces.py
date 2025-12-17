class movement_of_indivisual_pieces:
    def __init__(self, canvas):
        self.canvas = canvas
        self.X1, self.Y1 = 50, 50
        self.SIDE_LENGTH = 100
        self.X2, self.Y2 = 50 + self.SIDE_LENGTH, 50 + self.SIDE_LENGTH
    def pawn_moment(self, event):
        self.canvas.create_rectangle(self.X1, self.Y1, self.X2, self.Y2, fill="orange", width=2)