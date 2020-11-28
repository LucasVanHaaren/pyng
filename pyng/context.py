import pygame as pg
from abc import ABCMeta, abstractmethod
from time import time


class Context(metaclass=ABCMeta):
    """Represents a program activity

    Args:
        screen (pygame.Surface): Surface to draw the context
    """

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.clock = pg.time.Clock()
        self.running = False
        self.framerate = 60

        self.last_time = 0
        self.delta_time = 0

    @abstractmethod
    def run(self):
        """Run context, must be overrided.
        In most case you must call super().run()
        """
        self.running = True
        self.last_time = time()

    def register_event(self, event, delay):
        """Register any game event.
        May be object animation, object spawn.

        Args:
            event (int): event id (pygame.USEREVENT + 1)
            delay (int): delay time in miliseconds
        """
        pg.time.set_timer(event, delay)

    def _handle_events(self, events):
        """Handle pygame events

        Args:
            events (list(pygame.event)): A list of pygame events
        """
        for event in events:
            if event.type == pg.QUIT:
                self.running = False

    def _tick(self):
        """Tick the context clock according to the framerate"""
        self.clock.tick(self.framerate)

    def _compute_delta_time(self):
        """Compute delta_time, must be called before anything else."""
        self.delta_time = (time() - self.last_time) * 60
        self.last_time = time()
