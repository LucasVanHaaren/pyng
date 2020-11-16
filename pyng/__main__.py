import sys
import pygame as pg
import pyng.settings as s
from pyng.game import Game


def main():

    pg.init()
    pg.display.set_caption(s.SCREEN_CAPTION)
    screen = pg.display.set_mode(s.SCREEN_MODE)

    Game(screen).run()

    pg.quit()


if __name__ == "__main__":
    sys.exit(main())
