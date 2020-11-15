import pygame
import sys
from pyng.game import Game
from pyng import settings


def main():
    # set global params
    pygame.init()
    pygame.display.set_caption(settings.SCREEN_CAPTION)
    pygame.mouse.set_visible(settings.SCREEN_MOUSE_VISIBLE)

    # instantiate and run a game
    Game().run()

    pygame.quit()


if __name__ == "__main__":
    sys.exit(main())
