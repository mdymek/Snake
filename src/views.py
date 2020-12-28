"""
 Functions drawing visuals on the given display for game start and game stop views.
"""

import pygame
import src.constants as constants  # pylint: disable=import-error

pygame.init()  # pylint: disable=no-member

BIG_FONT = pygame.font.SysFont('Calibri', 35, True, False)
SMALL_FONT = pygame.font.SysFont('Calibri', 25, True, False)


def start_view(screen):
    """Start game view: instructions for the user."""
    screen.fill(constants.PINK)

    text = BIG_FONT.render("Are you ready for an adventure?", True, constants.BLACK)
    screen.blit(text, [90, 150])

    text = SMALL_FONT.render("Eat the red apples, avoid poison & obstacles.", True, constants.BLACK)
    screen.blit(text, [90, 250])

    text = SMALL_FONT.render("Try to gain as much points as possible!", True, constants.BLACK)
    screen.blit(text, [90, 280])

    text = SMALL_FONT.render("Press SPACE to start, Q to quit.", True, constants.BLACK)
    screen.blit(text, [90, 350])


def end_view(screen, score):
    """End game view: the score and users' options."""

    screen.fill(constants.PINK)

    text = BIG_FONT.render("GAME OVER", True, constants.BLACK)
    screen.blit(text, [100, 100])

    text = SMALL_FONT.render(f"Your score: {score}", True, constants.BLACK)
    screen.blit(text, [100, 150])

    text = SMALL_FONT.render("Press Q to quit, SPACE to start over", True, constants.BLACK)
    screen.blit(text, [100, 200])
