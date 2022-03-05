import pygame


"""
Displays the tic tac toe board in pygame
"""

class Board:
    def __init__(self, game_board, screen):
        # Initiallizes variables
        self.game_board = game_board
        self.screen = screen
        self.board = self.game_board.get_board()

        # initializes the images for the board
        self.o = pygame.image.load("photo/o.png")
        self.x = pygame.image.load("photo/x.png")
        self.blank = pygame.image.load("photo/square.png")
    
    # Turns the board variable into the display in pygame
    def render(self):
        self.board = self.game_board.get_board()
        for y in range(3):
            for x in range(3):
                if self.board[x][y] == 0:
                    self.screen.blit(self.blank, (y * 75 + 10, x * 75 + 10))
                if self.board[x][y] == 1:
                    self.screen.blit(self.o, (y * 75 + 10, x * 75 + 10))
                if self.board[x][y] == 2:
                    self.screen.blit(self.x, (y * 75 + 10, x * 75 + 10))

    # Incompleate function made to display an error that I couldn't get to work because pygame pauses with the wait function and breaks all my code
    def error(self, x, y, player):
        pass
        """
        if player == 1:
            self.screen.blit(self.o, (y * 75 + 10, x * 75 + 10))
        if player == 2:
            self.screen.blit(self.x, (y * 75 + 10, x * 75 + 10))
            """
