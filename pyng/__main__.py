import pygame
import sys
import time
from pyng.game import Paddle, Ball, Background
from pyng import settings


def main():
    pygame.init()

    pygame.display.set_caption(settings.SCREEN_CAPTION)
    screen = pygame.display.set_mode(settings.SCREEN_MODE)
    pygame.mouse.set_visible(settings.SCREEN_MOUSE_VISIBLE)
    clock = pygame.time.Clock()

    running = True
    framerate = 60
    last_time = time.time()

    # game objects (paddles, ball)
    objects = []
    background = Background(screen)
    paddle1 = Paddle(settings.PADDLE_COLORNAME, settings.PADDLE_BOTTOM_POS)
    ball = Ball()
    # paddle2 = Paddle(settings.PADDLE_COLORNAME, settings.PADDLE_TOP_POS)

    objects.append(background)  # IMPORTANT order: displayed as the same order
    objects.append(paddle1)
    objects.append(ball)
    # objects.append(paddle2)

    while running:

        delta_time = time.time() - last_time
        delta_time *= 60
        last_time = time.time()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle1.move_left()
        if keys[pygame.K_RIGHT]:
            paddle1.move_right()

        for obj in objects:
            obj.update(delta_time)
            screen.blit(obj.surface, obj.position)

        pygame.display.update()
        clock.tick(framerate)

    pygame.quit()


if __name__ == "__main__":
    sys.exit(main())
