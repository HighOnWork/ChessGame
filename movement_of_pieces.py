class movement_of_indivisual_pieces:
    def __init__(self, canvas):
        self.canvas = canvas
        # self.X1, self.Y1 = 0, 250
        self.SIDE_LENGTH = 125
        # self.X2, self.Y2 = self.X1 + self.SIDE_LENGTH, self.Y1 + self.SIDE_LENGTH
    def pawn_moment(self, event, pawn_y_position, pawn_x_position):
        X1, Y1 = pawn_x_position - 125 // 2, (pawn_y_position - 125 // 2) + self.SIDE_LENGTH
        X2, Y2 = X1 + self.SIDE_LENGTH, Y1 + self.SIDE_LENGTH
        if pawn_y_position <= 190:
            for _ in range(2):
                self.canvas.create_rectangle(X1, Y1, X2, Y2, fill="orange", width=2)
                Y1 += 125
                Y2 += 125
        else:
            self.canvas.create_rectangle(X1, Y1, X2, Y2, fill="orange", width=2)