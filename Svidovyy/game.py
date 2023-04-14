import pygame
import sys

from const import *
from board import Board


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.board = Board()

    def show_background(self):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = '#b5b9bb'
                else:
                    color = '#5c6163'

                rect = (col * SIZE, row * SIZE, SIZE, SIZE)

                pygame.draw.rect(self.screen, color, rect)

    def show_pieces(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    image = pygame.image.load(piece.texture)
                    image_center = col * SIZE + SIZE // 2, row * SIZE + SIZE // 2
                    piece.texture_rect = image.get_rect(center=image_center)
                    self.screen.blit(image, piece.texture_rect)

    def run(self):
        while True:
            self.show_background()
            self.show_pieces()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
