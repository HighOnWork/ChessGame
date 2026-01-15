# from chess_pieces import ChessPieces
# import tkinter as tk

from tkinter import FALSE, LAST


class movement_of_indivisual_pieces:
    def __init__(self, canvas):
        self.first_turn_done = False
        self.canvas = canvas
        self.spaces_to_move = []
        self.spaces_to_take = []
        self.move_count = 1
        self.lastID = None
        self.destroyPiece = False
        self.Flag = False
        self.RightFlag = False
        self.LeftFlag = False
        self.MOVE_RULES = {
            "p" : {'vectors': [(0, -1)], 'vectors_black': [(0, 1)], "sliding" : False, "black": True},
            "r" : {"vectors": [(0,1), (0,-1), (1,0), (-1,0)], "sliding": True, "black": False},
            "b" : {"vectors": [(1,1), (1,-1), (-1,1), (-1,-1)], "sliding": True, "black": False},
            "h" : {"vectors": [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)], "sliding": False, "black": False},
            "k" : {'vectors': [(1,1), (1,-1), (-1,1), (-1,-1), (0,1), (0,-1), (1,0), (-1,0)], "sliding" : False, "black": False},
            "q" : {"vectors": [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)], "sliding": True, "black": False},
        }

    def remove_spaces(self):
        if self.spaces_to_take:
                for space in self.spaces_to_take:
                    self.canvas.delete(space)
                self.spaces_to_take.clear()
        
        if self.spaces_to_move:
                for space in self.spaces_to_move:
                    self.canvas.delete(space)
                self.spaces_to_move.clear()

    def piece_to_the_side(self, x, y, size, unique_id, ccd):
        """ Checks for enemies diagonally in front of the pawn """
        # Calculate diagonal coordinates based on color
        direction = -1 if ccd[0] == 'w' else 1
        
        # Diagonal offsets: (Left-Diagonal, Right-Diagonal)
        diagonals = [
            (x - size, y + (direction * size)), # Left
            (x + size, y + (direction * size))  # Right
        ]
        for dx, dy in diagonals:
    # Only check if the coordinates are actually on the 8x8 board
            if 0 < dx < (size * 8) and 0 < dy < (size * 8):
                overlapping = self.canvas.find_overlapping(dx - 5, dy - 5, dx + 5, dy + 5)
                for item in overlapping:
                    tags = self.canvas.gettags(item)
                    if "pieces" in tags:
                        # Check if it's an enemy
                        if (ccd[0] == 'w' and 'bp' in tags) or (ccd[0] == 'b' and 'wp' in tags):
                            self.draw_capture_indicator(dx, dy, size, unique_id, item)

    def draw_capture_indicator(self, x, y, size, ID, target_piece_id):
        """ Creates the red square for captures and binds the click event """
        square = self.canvas.create_rectangle(
            x - size // 2, y - size // 2,
            x + size // 2, y + size // 2,
            fill="red", stipple="gray50", width=2
        )
        self.spaces_to_move.append(square)
        # Crucial: Bind the click to destroy the enemy piece
        self.canvas.tag_bind(square, "<Button-1>", 
            lambda event, s=square, id=ID, target=target_piece_id: 
            self.button_clicked(event, s, id, special_flag=True, lpi=target))



    def item_destroyed(self, event, square_id, unique_id):
        pass

    def piece_infront(self, square_id):
        square_coords = self.canvas.coords(square_id)  
        overlapping = self.canvas.find_overlapping(*square_coords)
        for item in overlapping:
            tags = self.canvas.gettags(item)
            if "pieces" in tags:
                self.Flag = True
                return tags, item
        return None

    def button_clicked(self, event, square_id, unique_id,  lpi=None, special_flag=False):
        print("Clicked on indicator")
        tags = self.canvas.gettags(unique_id)
        if "unmoved" in tags:
            self.canvas.dtag(unique_id, "unmoved")
        if special_flag and lpi:
            self.canvas.delete(lpi)
        square_id_coords = self.canvas.coords(square_id)
        print(square_id_coords)
        center_x = (square_id_coords[0] + square_id_coords[2]) / 2
        center_y = (square_id_coords[1] + square_id_coords[3]) / 2
        self.canvas.move(unique_id ,center_x - self.canvas.coords(unique_id)[0], center_y - self.canvas.coords(unique_id)[1])
        self.move_count += 1
        self.remove_spaces()

    def draw_indicator(self, x, y, size, ID, ccd):
        self.Flag = False
        self.RightFlag = False
        self.LeftFlag = False
        last_piece_id = None
        niche_id = None

        square = (self.canvas.create_rectangle(x - size // 2, 
                                                    y - size // 2, 
                                                    x + size // 2, 
                                                    y + size // 2, 
                                                    fill="orange", 
                                                    stipple="gray50",
                                                    width=2))
        self.spaces_to_move.append(square)
        self.canvas.tag_bind(square, "<Button-1>", lambda event, s=square, id=ID: self.button_clicked(event, s, id))

        result = self.piece_infront(square_id=square)

        tags = self.canvas.gettags(ID)

        orig_index = self.spaces_to_move.index(square)
        item = self.spaces_to_move[orig_index]
        

        if result is not None:
            last_piece_id, niche_id = result
        
        if last_piece_id is not None:
            print(last_piece_id)

            piece_color = last_piece_id[0][0] if last_piece_id and last_piece_id[0] else None
            if piece_color == ccd[0] or ccd[1] == "p":

                self.spaces_to_move.pop(orig_index)
                self.canvas.delete(item)
 
            elif piece_color != ccd[0]:
                self.canvas.itemconfig(square, fill="red")
                self.canvas.tag_bind(item, "<Button-1>", lambda event, s=square, id=ID: self.button_clicked(event, s, id, special_flag = True, lpi=niche_id))

        

    def move_pieces(self, event, unique_id, ccd, square_size):
        self.remove_spaces()
        coords = self.canvas.coords(unique_id)
        start_x, start_y = coords[0], coords[1]
        is_white = ccd[0] == 'w'

        # 1. HANDLE PAWN CAPTURES (Diagonal)
        if ccd[1] == 'p':
            self.piece_to_the_side(start_x, start_y, square_size, unique_id, ccd)

        # 2. HANDLE STANDARD MOVEMENT (Forward/Vectors)
        if (self.move_count % 2 == 0 and not is_white) or (self.move_count % 2 != 0 and is_white):
            rules = self.MOVE_RULES[ccd[1]]
            key = "vectors_black" if (not is_white and rules.get("black")) else "vectors"

            for vx, vy in rules[key]:
                cur_x, cur_y = start_x, start_y
                
                # For pawns, we only check 1 or 2 squares forward
                max_steps = 1
                if ccd[1] == 'p' and "unmoved" in self.canvas.gettags(unique_id):
                    max_steps = 2
                
                # For sliding pieces (Rook/Queen), use a high number
                if rules.get("sliding"): max_steps = 8

                for step in range(max_steps):
                    cur_x += (vx * square_size)
                    cur_y += (vy * square_size)
                    
                    if not (0 < cur_x < 1000 and 0 < cur_y < 1000): break

                    # Pawns cannot move forward if blocked (Flag logic)
                    self.Flag = False
                    self.draw_indicator(cur_x, cur_y, square_size, unique_id, ccd)
                    
                    if self.Flag: # If square is blocked
                        # If it's a pawn moving forward, delete the orange indicator (can't jump)
                        if ccd[1] == 'p':
                            item = self.spaces_to_move.pop()
                            self.canvas.delete(item)
                        break 
                    
                    if not rules.get("sliding") and ccd[1] != 'p':
                        break