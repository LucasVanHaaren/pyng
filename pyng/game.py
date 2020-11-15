import pygame
import pyng.settings


class GameObject:
    def __init__(self, surface, start_pos):
        self.surface = surface
        self.position = self.surface.get_rect().move(start_pos)


class Background(GameObject):
    def __init__(self, screen):
        super().__init__(pygame.Surface(screen.get_size()).convert(), (0, 0))
        self.surface.fill(pyng.settings.BACKGROUND_COLORNAME)
        pygame.draw.line(
            self.surface,
            pygame.color.THECOLORS[pyng.settings.BACKGROUND_LINE_COLORNAME],
            (0, 325),
            (450, 325),
        )

    def update(self, delta_time):
        pass


class Ball(GameObject):
    def __init__(self):
        super().__init__(
            pygame.Surface(pyng.settings.BALL_SIZE), pyng.settings.BALL_START_POS
        )
        self.color = pygame.color.THECOLORS[pyng.settings.BALL_COLORNAME]
        self.surface.fill(self.color)

    def update(self, delta_time):
        pass


class Paddle(GameObject):
    def __init__(self, colorname, start_pos):
        super().__init__(pygame.Surface(pyng.settings.PADDLE_SIZE), start_pos)
        self.color = pygame.color.THECOLORS[colorname]
        self.x_velocity = 0
        self.surface.fill(self.color)

    def move_left(self):
        self.x_velocity -= 2

    def move_right(self):
        self.x_velocity += 2

    def update(self, delta_time):
        self.position = self.position.move(self.x_velocity * delta_time, 0)

        # decrease velocity if it's in movement
        if self.x_velocity > 0:
            self.x_velocity -= 1
        elif self.x_velocity < 0:
            self.x_velocity += 1
