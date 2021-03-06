"""
The game logic of tictactoe is held and managed in this class
"""

class TicTacToe:
    def __init__(self):
        self.game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    def checkWin(self):
        # if there is 3 of the same in a row return the player that won
        if self.game[0][0] > 0 and self.game[0][0]==self.game[0][1]==self.game[0][2]:
            return self.game[0][0]
        if self.game[1][0] > 0 and self.game[1][0]==self.game[1][1]==self.game[1][2]:
            return self.game[1][0]
        if self.game[2][0] > 0 and self.game[2][0]==self.game[2][1]==self.game[2][2]:
            return self.game[2][0]
        
        # if there is 3 of the same in a column return the player that won
        if self.game[0][0] > 0 and self.game[0][0]==self.game[1][0]==self.game[2][0]:
            return self.game[0][0]
        if self.game[0][1] > 0 and self.game[0][1]==self.game[1][1]==self.game[2][1]:
            return self.game[0][1]
        if self.game[0][2] > 0 and self.game[0][2]==self.game[1][2]==self.game[2][2]:
            return self.game[0][2]
        
        # if there is a winner diagnally, return the winner
        if self.game[0][0] > 0 and self.game[0][0]==self.game[1][1]==self.game[2][2]:
            return self.game[0][0]
        if self.game[2][0] > 0 and self.game[2][0]==self.game[1][1]==self.game[0][2]:
            return self.game[2][0]

        # if there is a tie, return 3
        is_moveable = False
        
        for i in self.game:
            for j in i:
                if j == 0:
                    is_moveable = True
                
        if not is_moveable:
            return 3
        
        # if there isn't a winner, return 0
        return 0

    def move(self, posx, posy, player):
        # if a player has moved there, return -1
        if self.game[posy][posx] > 0:
            return -1
        # makes the move, checks if there is a winner
        self.game[posy][posx] = player
        return self.checkWin()
    
    # game output as a string (for when someone wins)
    def __str__(self):
        return (f"Game: \n{self.game[0][0]}|{self.game[0][1]}|{self.game[0][2]} \n{self.game[1][0]}|{self.game[1][1]}|{self.game[1][2]} \n{self.game[2][0]}|{self.game[2][1]}|{self.game[2][2]}")

    # board variable getter
    def get_board(self):
        return self.game
    
    # resets the board
    def reset(self):
        self.game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]