import time
import pygame as pg
import pyng.settings as s
from pyng.paddle import Paddle, PaddleSide
from pyng.ball import Ball
from pyng.ui import BackgroundUI, ScoreUI


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.clock = pg.time.Clock()
        self.running = False
        self.framerate = 60

        self.background_ui = BackgroundUI("cadetblue", "white")
        self.score_ui = ScoreUI("white")

        self.paddle1 = Paddle("white", PaddleSide.BOTTOM)
        self.paddle2 = Paddle("white", PaddleSide.TOP)
        self.ball = Ball("white")

        self.game_objects = pg.sprite.RenderUpdates()
        self.game_objects.add(
            self.background_ui, self.score_ui, self.paddle1, self.paddle2, self.ball
        )

        self.ui_objects = pg.sprite.Group()
        self.ui_objects.add(self.background_ui, self.score_ui)

        self.paddles = pg.sprite.Group()
        self.paddles.add(self.paddle1, self.paddle2)

    def run(self):
        self.running = True
        last_time = time.time()

        while self.running:
            delta_time, last_time = self._get_delta_time(last_time)

            for e in pg.event.get():
                if e.type == pg.QUIT:
                    self.running = False

            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                self.paddle1.move_left()
            if keys[pg.K_RIGHT]:
                self.paddle1.move_right()
            if keys[pg.K_a]:
                self.paddle1.score += 1
                self.score_ui.set_score([self.paddle1.score, self.paddle2.score])

            self.game_objects.update(delta_time)

            dirty = self.game_objects.draw(self.screen)
            pg.display.update(dirty)
            self.clock.tick(self.framerate)

    def _get_delta_time(self, last_time):
        """Compute delta_time, return delta time and last time"""
        return ((time.time() - last_time) * 60, time.time())
