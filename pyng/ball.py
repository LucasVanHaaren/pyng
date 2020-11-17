import pygame as pg
import pyng.settings as s


class Ball(pg.sprite.Sprite):
    """Ball game object"""

    MAX_VELOCITY = 8

    def __init__(self, color):
        super().__init__()
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.image = pg.Surface(s.BALL_SIZE).convert()
        self.rect = self.image.get_rect()
        self.x_velocity = 0
        self.y_velocity = 0

        self.image.fill(pg.Color(color))
        self.reset()

    def reset(self):
        self.rect.center = self.screen_rect.center

    def update(self, delta_time):
        pass
