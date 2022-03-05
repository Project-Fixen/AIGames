import pygame
from game import TicTacToe
from board import Board

"""
Main function, manages the controlls
    Mouse: clicking to make your move
    R: to reset the board
    Q: to quit
"""


def main():
    # initializes variables
    screen = pygame.display.set_mode((235, 235))
    game_board = TicTacToe()
    display = Board(game_board, screen)

    player = 1

    running = True

    display.render()

    # GUI Loop
    while True:
        # for each event from pygame
        for event in pygame.event.get():
            # if click x (top right of gui) button, quit
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # if press a key run the command for the key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: 
                    pygame.quit()
                    return
                if event.key == pygame.K_r:
                    game_board.reset()
                    display.render()
                    running = True
            
            # if click mouse and game is active, make the move based on who went last for the piece
            if event.type == pygame.MOUSEBUTTONDOWN and running:
                mousepos = pygame.mouse.get_pos()
                x = (mousepos[0] - 10) // 75
                y = (mousepos[1] - 10) // 75

                # TODO: make mouse fail to place when click border

                if (x >= 3 or y >= 3):
                    result = -1
                else:
                    result = game_board.move(x, y, player) 
                if result == -1:
                    display.error(x, y, player)
                else:
                    player += 1
                    if player > 2:
                        player = 1
                # if Game has ended, print info on game and turn running to false
                if result > 0:
                    running = False
                    if result == 3:
                        print("Nobody wins! Its a tie")
                        print(game_board)
                    else:
                        print(f"Player {result} wins!")
                        print(game_board)
                # Update the display of the game board
                display.render()
        # update GUI
        pygame.display.update()
    


if __name__ == "__main__":
    main()