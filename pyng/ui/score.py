import pygame as pg
import pyng.settings as s


class Score(pg.sprite.Sprite):
    """UI component to draw score"""

    def __init__(self, color):
        super().__init__()
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.font = pg.font.Font(pg.font.get_default_font(), 20)
        self.color = pg.Color(color)
        self.last_score = []
        self.score = [0, 0]
        self.update(0)
        self.rect = self.image.get_rect().move(0, self.screen_rect.centery)

    def set_score(self, score):
        self.score = score

    def update(self, delta_time):
        if self.score != self.last_score:
            self.last_score = self.score
            self.image = self.font.render(
                f"{self.score[0]} - {self.score[1]}", True, self.color
            )
