import time
import pygame as pg
import pyng.settings as s
from pyng.paddle import Paddle, PaddleSide
from pyng.ball import Ball
from pyng.ui import BackgroundUI, ScoreUI
from pyng.map import get_side_boundaries, get_goal_boundaries


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.clock = pg.time.Clock()
        self.running = False
        self.framerate = 60

        self.background_ui = BackgroundUI("cadetblue", "white")
        self.score_ui = ScoreUI("white")

        self.side_boundaries = get_side_boundaries(self.screen_rect)
        self.goal_boundaries = get_goal_boundaries(self.screen_rect)

        self.paddle1 = Paddle("white", PaddleSide.BOTTOM, pg.K_LEFT, pg.K_RIGHT)
        self.paddle2 = Paddle("white", PaddleSide.TOP, pg.K_q, pg.K_d)
        self.ball = Ball("white")

        self.game_objects = pg.sprite.RenderUpdates()
        self.game_objects.add(
            self.background_ui,
            # self.side_boundaries,
            # self.goal_boundaries,
            self.score_ui,
            self.paddle1,
            self.paddle2,
            self.ball,
        )

        self.ui_objects = pg.sprite.Group()
        self.ui_objects.add(self.background_ui, self.score_ui)

        self.paddles = pg.sprite.Group()
        self.paddles.add(self.paddle1, self.paddle2)

        self.map_bounds = pg.sprite.Group()
        self.map_bounds.add(self.side_boundaries)
        self.map_bounds.add(self.goal_boundaries)

    def run(self):
        self.running = True
        last_time = time.time()
        self.ball.serve()
        while self.running:
            delta_time, last_time = self._get_delta_time(last_time)
            self._handle_events(pg.event.get())
            self._handle_key_pressed(pg.key.get_pressed())
            self.game_objects.update(delta_time)
            self._handle_collides(delta_time)

            dirty = self.game_objects.draw(self.screen)
            pg.display.update(dirty)
            self.clock.tick(self.framerate)

    def _handle_collides(self, delta_time):
        for paddle in pg.sprite.groupcollide(
            self.paddles, self.map_bounds, False, False
        ):
            paddle.move_reverse()
            paddle.update(delta_time)
        if pg.sprite.spritecollide(self.ball, self.paddles, False):
            self.ball.bounce()
        if pg.sprite.spritecollide(self.ball, self.map_bounds, False, False):
            self.ball.bounce()
        for goal in pg.sprite.spritecollide(self.ball, self.goal_boundaries, False):
            for paddle in self.paddles:
                if paddle.side == goal.opponent:
                    paddle.score += 1
            self.score_ui.set_score([self.paddle1.score, self.paddle2.score])

    def _handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.running = False

    def _handle_key_pressed(self, keys):
        for paddle in self.paddles:
            if keys[paddle.move_left_key]:
                paddle.move_left()
            if keys[paddle.move_right_key]:
                paddle.move_right()

    def _get_delta_time(self, last_time):
        """Compute delta_time, return delta time and last time"""
        return ((time.time() - last_time) * 60, time.time())
