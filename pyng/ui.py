import pygame as pg
import pyng.settings as s


class BackgroundUI(pg.sprite.Sprite):
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


class ScoreUI(pg.sprite.Sprite):
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
