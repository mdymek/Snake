import pygame
from src.snake import Snake
from src.field import Field
import src.constants as constants
import src.views as views

"""
 todo doc

"""

size = (800, 800)
game_on, user_start = True, False

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Adventures of a small Python")
clock = pygame.time.Clock()

while game_on:
    score = 0
    user_exit, user_quit = False, False

    snake = Snake()
    field = Field()

    while not user_start:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                user_start, user_exit, user_quit, game_on = True, True, True, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    user_start, user_exit, user_quit, game_on = True, True, True, False
                elif event.key == pygame.K_SPACE:
                    user_start = True

        views.start_view(screen)
        pygame.display.flip()

        clock.tick(constants.TICKS_PER_MIN)

    while not user_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                user_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    user_exit = True
                else:
                    snake.move(event.key)

        screen.fill(constants.GREEN)

        field.draw(screen)
        new_position = snake.draw(screen)

        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render(f"Your score: {score}", True, constants.BLACK)
        screen.blit(text, [0, 0])

        pygame.display.flip()

        event = field.check_event(new_position)
        if event == 1:
            user_exit = True
        elif event == 2:
            if snake.poison():
                user_exit = True
            score -= 30
        elif event == 3:
            snake.eat()
            score += 10

        if snake.crash(new_position):
            user_exit = True

        clock.tick(constants.TICKS_PER_MIN)

    while not user_quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                user_quit, game_on = True, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    user_quit, game_on = True, False
                elif event.key == pygame.K_SPACE:
                    user_quit = True

        views.end_view(screen, score)
        pygame.display.flip()

        clock.tick(constants.TICKS_PER_MIN)

pygame.quit()
