import pygame as pg
import pyng.settings as s
from enum import Enum, unique, auto


class Paddle(pg.sprite.Sprite):
    """Paddle game object"""

    SCALE_FACTOR = (1 / 9, 1 / 65)  # means a paddle is 1/9 the screen size wide ect

    MAX_VELOCITY = 15
    INC_VELOCITY = 2
    DEC_VELOCITY = 1

    def __init__(self, color, side):
        super().__init__()
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()

        self.image = pg.Surface(
            (
                self.screen_rect.width * self.SCALE_FACTOR[0],
                self.screen_rect.height * self.SCALE_FACTOR[1],
            )
        ).convert()
        self.rect = self.image.get_rect()

        self.side = side
        self.score = 0
        self.x_velocity = 0

        self.image.fill(pg.Color(color))
        self.reset()

    def reset(self):
        self.rect.centerx = self.screen_rect.centerx
        if self.side == PaddleSide.TOP:
            self.rect.top = self.rect.top + (
                self.SCALE_FACTOR[1] * self.screen_rect.height
            )
        elif self.side == PaddleSide.BOTTOM:
            self.rect.bottom = self.screen_rect.bottom - (
                self.SCALE_FACTOR[1] * self.screen_rect.height
            )
        else:
            raise ValueError("Paddle.side must be of type PaddleSide")

    def move_left(self):
        if abs(self.x_velocity) <= (self.MAX_VELOCITY - self.INC_VELOCITY):
            self.x_velocity -= self.INC_VELOCITY

    def move_right(self):
        if abs(self.x_velocity) <= (self.MAX_VELOCITY - self.INC_VELOCITY):
            self.x_velocity += self.INC_VELOCITY

    def move_reverse(self):
        if abs(self.x_velocity) > self.INC_VELOCITY:
            self.x_velocity = -self.x_velocity

    def _decrease_x_velocity(self):
        # slow down if paddle is in movement
        if self.x_velocity >= (0 + self.DEC_VELOCITY):
            self.x_velocity -= self.DEC_VELOCITY
        elif self.x_velocity <= (0 - self.DEC_VELOCITY):
            self.x_velocity += self.DEC_VELOCITY

    def _handle_bounds_collide(self):
        if self.rect.left <= self.screen_rect.left:
            self.rect.left = self.screen_rect.left
            self.move_reverse()
        if self.rect.right >= self.screen_rect.right:
            self.rect.right = self.screen_rect.right
            self.move_reverse()

    def update(self, delta_time):
        self._handle_bounds_collide()
        self.rect = self.rect.move(self.x_velocity * delta_time, 0)
        self._decrease_x_velocity()


@unique
class PaddleSide(Enum):
    TOP = auto()
    BOTTOM = auto()
