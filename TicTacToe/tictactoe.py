import pygame
from game import TicTacToe
from board import Board


def main():
    screen = pygame.display.set_mode((236, 236))
    game_board = TicTacToe()
    display = Board(game_board, screen)

    player = 1

    running = True

    display.render()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: 
                    pygame.quit()
                    return
                if event.key == pygame.K_r:
                    game_board.reset()
                    display.render()
                    running = True
            
            if event.type == pygame.MOUSEBUTTONDOWN and running:
                mousepos = pygame.mouse.get_pos()
                x = (mousepos[0] - 10) // 75
                y = (mousepos[1] - 10) // 75
                result = game_board.move(x, y, player) 
                if result == -1:
                    display.error(x, y, player)
                else:
                    player += 1
                    if player > 2:
                        player = 1
                if result > 0:
                    running = False
                    if result == 3:
                        print("Nobody wins! Its a tie")
                        print(game_board)
                    else:
                        print(f"Player {result} wins!")
                        print(game_board)
                display.render()
        pygame.display.update()
    


if __name__ == "__main__":
    main()