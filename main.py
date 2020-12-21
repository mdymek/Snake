import pygame
from src.snake import Snake
from src.field import Field
from random import randint

"""
 todo doc

"""

pygame.init()

BLACK = (0, 0, 0)
GREEN = (51, 153, 51)

ticks_per_min = 10

size = (800, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Adventures of a small Python")

user_exit = False
clock = pygame.time.Clock()

score = 0

snake = Snake()
field = Field()

while not user_exit:
    if randint(0, 100) < 1:
        field.add_poison()

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:
            user_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                user_exit = True
            else:
                snake.move(event.key)

    screen.fill(GREEN)

    field.draw(screen)
    new_position = snake.draw(screen)

    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(f"Your score: {score}", True, BLACK)
    screen.blit(text, [0, 0])

    pygame.display.flip()

    # HANDLE EVENT
    event = field.check_event(new_position)
    if event == 1:
        # end game
        user_exit = True
    elif event == 2:
        # poison
        if snake.poison():
            user_exit = True
        score -= 30
    elif event == 3:
        # eat apple
        snake.eat()
        score += 10

    if snake.crash(new_position):
        # end game
        user_exit = True

    clock.tick(ticks_per_min)

pygame.quit()
