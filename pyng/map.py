import pygame as pg
import pyng.settings as s

WALL_WIDTH = 5


class Wall(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.image = pg.Surface([width, height]).convert()
        self.image.fill(pg.Color("red3"))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y


def get_side_boundaries(screen_rect):
    bounds = []
    bounds.append(Wall(0, 0, WALL_WIDTH, screen_rect.height))
    bounds.append(Wall(screen_rect.width - WALL_WIDTH, 0, WALL_WIDTH, 650))
    return bounds


def get_goal_boundaries(screen_rect):
    bounds = []
    bounds.append(Wall(0, 0, screen_rect.width, WALL_WIDTH))
    bounds.append(
        Wall(0, screen_rect.height - WALL_WIDTH, screen_rect.width, WALL_WIDTH)
    )
    return bounds
