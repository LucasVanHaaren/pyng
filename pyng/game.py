import pygame as pg

from pyng.context import Context
from pyng.objects.paddle import Paddle, PaddleSide
from pyng.objects.ball import Ball
from pyng.ui.background import Background
from pyng.ui.score import Score


class Game(Context):
    def __init__(self, screen):
        super().__init__(screen)

        self.background = Background("cadetblue", "white")
        self.score = Score("white")
        self.paddle_bot = Paddle("white", PaddleSide.BOTTOM)
        self.paddle_top = Paddle("white", PaddleSide.TOP)
        self.ball = Ball("white")

        self.paddles = pg.sprite.Group(self.paddle_top, self.paddle_bot)
        self.ui_objects = pg.sprite.Group(self.background, self.score)
        self.game_objects = pg.sprite.RenderUpdates(
            self.ui_objects, self.paddles, self.ball
        )

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
            self.paddle_bot.move_left()
        if keys[pg.K_RIGHT]:
            self.paddle_bot.move_right()
