import pygame as pg
import pyng.settings as s


class Ball(pg.sprite.Sprite):
    """Ball game object"""

    SCALE_FACTOR = 1 / 45

    MAX_VELOCITY = 8

    def __init__(self, color):
        super().__init__()
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()

        self.image = pg.Surface(
            (
                self.screen_rect.width * self.SCALE_FACTOR,
                self.screen_rect.width * self.SCALE_FACTOR,
            )
        ).convert()
        self.rect = self.image.get_rect()

        self.image.fill(pg.Color(color))
        self.reset()

        self.velocity = pg.math.Vector2()
        self.pos = pg.math.Vector2(self.rect.x, self.rect.y)

    def reset(self):
        self.rect.center = self.screen_rect.center

    def update(self, delta_time):
        pass
