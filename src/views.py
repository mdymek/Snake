import src.constants as constants
import pygame

pygame.init()

big_font = pygame.font.SysFont('Calibri', 35, True, False)
small_font = pygame.font.SysFont('Calibri', 25, True, False)


def start_view(screen):
    screen.fill(constants.PINK)

    text = big_font.render(f"Are you ready for an adventure?", True, constants.BLACK)
    screen.blit(text, [90, 150])

    text = small_font.render("Eat the red apples and avoid poison and obstacles.", True, constants.BLACK)
    screen.blit(text, [90, 250])

    text = small_font.render("Try to gain as much points as possible!", True, constants.BLACK)
    screen.blit(text, [90, 280])

    text = small_font.render("Press SPACE to start, Q to quit.", True, constants.BLACK)
    screen.blit(text, [90, 350])


def end_view(screen, score):
    screen.fill(constants.PINK)

    text = big_font.render("GAME OVER", True, constants.BLACK)
    screen.blit(text, [100, 100])

    text = small_font.render(f"Your score: {score}", True, constants.BLACK)
    screen.blit(text, [100, 150])

    text = small_font.render("Press Q to quit, SPACE to start over", True, constants.BLACK)
    screen.blit(text, [100, 200])
