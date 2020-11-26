import time
import pygame as pg
import pyng.settings as s

from pyng.context import Context
from pyng.paddle import Paddle, PaddleSide
from pyng.ball import Ball
from pyng.ui import BackgroundUI, ScoreUI


class Game(Context):
    def __init__(self, screen):
        super().__init__(screen)
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
        super().run()
        while self.running:
            self._compute_delta_time()
            self._handle_events(pg.event.get())
            self._handle_keypressed(pg.key.get_pressed())

            self.game_objects.update(self.delta_time)
            dirty = self.game_objects.draw(self.screen)
            pg.display.update(dirty)
            self._tick()

    def _handle_keypressed(self, keys):
        if keys[pg.K_LEFT]:
            self.paddle1.move_left()
        if keys[pg.K_RIGHT]:
            self.paddle1.move_right()
