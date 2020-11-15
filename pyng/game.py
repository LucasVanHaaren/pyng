import pygame
import time
from pyng import settings


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(settings.SCREEN_MODE)
        self.clock = pygame.time.Clock()
        self.running = False
        self.framerate = 60
        self.game_objects = []
        self.paddle1 = Paddle(settings.PADDLE_COLORNAME, settings.PADDLE_BOTTOM_POS)
        self.paddle2 = Paddle(settings.PADDLE_COLORNAME, settings.PADDLE_TOP_POS)
        self.ball = Ball()
        self.background = Background(self.screen)

        self._load()

    def _load(self):
        self.game_objects.append(self.background)
        self.game_objects.append(self.paddle1)
        self.game_objects.append(self.paddle2)
        self.game_objects.append(self.ball)

    def _get_boundaries(self):
        pass

    def _get_delta_time(self, last_time):
        return (time.time() - last_time) * 60

    def run(self):
        self.running = True
        last_time = time.time()
        while self.running:
            delta_time = self._get_delta_time(last_time)
            last_time = time.time()

            # handle window exit event
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False

            # handle key pressed
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.paddle1.move_left()
            if keys[pygame.K_RIGHT]:
                self.paddle1.move_right()
            if keys[pygame.K_q]:
                self.paddle2.move_left()
            if keys[pygame.K_d]:
                self.paddle2.move_right()

            # update loop
            for obj in self.game_objects:
                obj.update(delta_time)

            # display loop
            for obj in self.game_objects:
                self.screen.blit(obj.surface, obj.position)

            pygame.display.update()
            self.clock.tick(self.framerate)


class GameObject:
    def __init__(self, surface, start_pos):
        self.surface = surface
        self.position = self.surface.get_rect().move(start_pos)


class Background(GameObject):
    def __init__(self, screen):
        super().__init__(pygame.Surface(screen.get_size()).convert(), (0, 0))
        self.surface.fill(settings.BACKGROUND_COLORNAME)
        pygame.draw.line(
            self.surface,
            pygame.color.THECOLORS[settings.BACKGROUND_LINE_COLORNAME],
            (0, 325),
            (450, 325),
        )

    def update(self, delta_time):
        pass


class Ball(GameObject):
    def __init__(self):
        super().__init__(pygame.Surface(settings.BALL_SIZE), settings.BALL_START_POS)
        self.color = pygame.color.THECOLORS[settings.BALL_COLORNAME]
        self.surface.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.surface, self.color, (5, 5), 5)

    def update(self, delta_time):
        pass


class Paddle(GameObject):

    MAX_X_VELOCITY = 15
    INC_X_VELOCITY_FACTOR = 2
    DEC_X_VELOCITY_FACTOR = 1

    def __init__(self, colorname, start_pos):
        super().__init__(pygame.Surface(settings.PADDLE_SIZE), start_pos)
        self.color = pygame.color.THECOLORS[colorname]
        self.x_velocity = 0
        self.surface.fill(self.color)

    def move_left(self):
        if abs(self.x_velocity) <= self.MAX_X_VELOCITY:
            self.x_velocity -= self.INC_X_VELOCITY_FACTOR

    def move_right(self):
        if abs(self.x_velocity) <= self.MAX_X_VELOCITY:
            self.x_velocity += self.INC_X_VELOCITY_FACTOR

    def decrease_x_velocity(self):
        # decrease velocity if it's in movement
        if self.x_velocity > 0:
            self.x_velocity -= self.DEC_X_VELOCITY_FACTOR
        elif self.x_velocity < 0:
            self.x_velocity += self.DEC_X_VELOCITY_FACTOR

    def update(self, delta_time):
        self.position = self.position.move(self.x_velocity * delta_time, 0)
        self.decrease_x_velocity()
