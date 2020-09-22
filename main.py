import pygame
from checkers import *
from checkers.game import Game


class Run:
    FPS = 60
    pygame.display.set_caption('Checkers')

    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    def main(self):
        run = True
        clock = pygame.time.Clock()
        game = Game(self.win)

        while run:
            clock.tick(self.FPS)
            if game.winner() is not None:
                print(game.winner())
                run = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_row_col_from_mouse(pos)
                    game.select(row, col)

            game.update()

        pygame.quit()


if __name__ == '__main__':
    run = Run()
    run.main()
