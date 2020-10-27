import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax
from menu_assets.menu import OptionsMenu
from menu_assets.menu import Menu
from menu_assets.logics import Logics


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


class MainGame:
    RUN = True
    CLOCK = pygame.time.Clock()
    GAME = Game(WIN)

    @staticmethod
    def get_row_col_from_mouse(pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    def main(self):
        logics = Logics()

        while logics.running:
            logics.curr_menu.display_menu()
            logics.game_loop()

        while self.RUN:
            self.CLOCK.tick(FPS)
            if self.GAME.turn == WHITE:
                value, new_board = minimax(self.GAME.get_board(), logics.options.difficulty,
                                           WHITE, self.GAME)
                if new_board is None:
                    print("TIE")
                    break

                self.GAME.ai_move(new_board)

            if self.GAME.winner() is not None:
                print(self.GAME.winner())
                self.RUN = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUN = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_row_col_from_mouse(pos)
                    self.GAME.select(row, col)

            self.GAME.update()

        pygame.quit()


if __name__ == '__main__':
    MainGame().main()
