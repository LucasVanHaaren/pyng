import pygame as pg
import pyng.settings as s


class Background(pg.sprite.Sprite):
    """UI component to draw game background"""

    def __init__(self, bg_color, line_color):
        super().__init__()
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.image = pg.Surface(self.screen.get_size()).convert()
        self.rect = self.image.get_rect()

        self.image.fill(pg.Color(bg_color))
        pg.draw.line(
            self.image,
            pg.Color(line_color),
            (0, self.screen_rect.centery),
            (self.screen_rect.width, self.screen_rect.centery),
        )

    def update(self, delta_time):
        pass