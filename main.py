from random import randint
import pygame
from src.snake import Snake
from src.field import Field
import src.constants as constants

"""
 todo doc

"""

score = 0
size = (800, 800)
user_exit = False

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Adventures of a small Python")
clock = pygame.time.Clock()

snake = Snake()
field = Field()

while not user_exit:
    if randint(0, 100) < 2:
        field.add_poison()

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

    clock.tick(constants.TICKS_PER_MIN)

screen.fill(constants.GREEN)

font = pygame.font.SysFont('Calibri', 25, True, False)
text = font.render(f"Your score: {score}", True, constants.BLACK)
screen.blit(text, [100, 150])

font = pygame.font.SysFont('Calibri', 35, True, False)
text = font.render("GAME OVER", True, constants.BLACK)
screen.blit(text, [100, 100])
pygame.display.flip()

pygame.quit()
