import pygame as pg
import pyng.settings as s
from enum import Enum, unique, auto


class Paddle(pg.sprite.Sprite):
    """Paddle game object"""

    POSITION_MARGIN = 10

    MAX_X_VELOCITY = 15
    INC_X_VELOCITY = 2
    DEC_X_VELOCITY = 1

    def __init__(self, color, side, move_left_key, move_right_key):
        super().__init__()
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.image = pg.Surface(s.PADDLE_SIZE).convert()
        self.rect = self.image.get_rect()
        self.side = side
        self.score = 0
        self.x_velocity = 0

        self.move_left_key = move_left_key
        self.move_right_key = move_right_key

        self.image.fill(pg.Color(color))
        self.reset()

    def reset(self):
        self.rect.centerx = self.screen_rect.centerx
        if self.side == PaddleSide.TOP:
            self.rect.top = self.rect.top + self.POSITION_MARGIN
        elif self.side == PaddleSide.BOTTOM:
            self.rect.bottom = self.screen_rect.bottom - self.POSITION_MARGIN
        else:
            raise ValueError("Paddle.side must be of type PaddleSide")

    def move_left(self):
        if abs(self.x_velocity) <= (self.MAX_X_VELOCITY - self.INC_X_VELOCITY):
            self.x_velocity -= self.INC_X_VELOCITY

    def move_right(self):
        if abs(self.x_velocity) <= (self.MAX_X_VELOCITY - self.INC_X_VELOCITY):
            self.x_velocity += self.INC_X_VELOCITY

    def move_reverse(self):
        if self.x_velocity > 0:
            self.x_velocity = -(self.x_velocity + self.INC_X_VELOCITY)
        elif self.x_velocity < 0:
            self.x_velocity = -self.x_velocity + self.INC_X_VELOCITY

    def _decrease_x_velocity(self):
        # slow down if paddle is in movement
        if self.x_velocity >= (0 + self.DEC_X_VELOCITY):
            self.x_velocity -= self.DEC_X_VELOCITY
        elif self.x_velocity <= (0 - self.DEC_X_VELOCITY):
            self.x_velocity += self.DEC_X_VELOCITY

    def update(self, delta_time):
        self.rect = self.rect.move(self.x_velocity * delta_time, 0)
        self._decrease_x_velocity()


@unique
class PaddleSide(Enum):
    TOP = auto()
    BOTTOM = auto()
