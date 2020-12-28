"""
The main class of the game -- initializing the game and controlling its flow.
"""

import pygame
from src.snake import Snake  # pylint: disable=import-error
from src.field import Field  # pylint: disable=import-error
import src.constants as consts  # pylint: disable=import-error
import src.views as views  # pylint: disable=import-error


class Game:
    """
    Game instance holds all of the variables controlling the flow of the game, and invokes methods
    responsible for all different views.
    It creates instances of Snake and Field and uses their methods to execute the gameplay.
    """

    def __init__(self):
        self.score = 0
        self.snake, self.field = None, None
        self.game_on, self.user_start, self.user_exit, self.user_quit = True, False, False, False

    def show_start_view(self, screen):
        """ Displays the start game screen and handles user input. """
        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pylint: disable=no-member
                self.user_start, self.user_exit, self.user_quit = True, True, True
                self.game_on = False
            if event.type == pygame.KEYDOWN:  # pylint: disable=no-member
                if event.key == pygame.K_q:  # pylint: disable=no-member
                    self.user_start, self.user_exit, self.user_quit = True, True, True
                    self.game_on = False
                elif event.key == pygame.K_SPACE:  # pylint: disable=no-member
                    self.user_start = True

        # Draw on the display
        views.start_view(screen)
        pygame.display.flip()

    def show_game_view(self, screen):
        """ Displays the main game screen and handles user input. """
        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pylint: disable=no-member
                self.user_exit, self.user_quit, self.game_on = True, True, False
            if event.type == pygame.KEYDOWN:  # pylint: disable=no-member
                if event.key == pygame.K_q:  # pylint: disable=no-member
                    self.user_exit = True
                else:
                    self.snake.move(event.key)

        # Draw on the display
        self.field.draw(screen)
        new_position = self.snake.draw(screen)

        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render(f"Your score: {self.score}", True, consts.BLACK)
        screen.blit(text, [0, 0])

        pygame.display.flip()

        # Handle events caused by snake movement
        event = self.field.check_event(new_position)

        if event == Field.Event.OBSTACLE_HIT:
            self.user_exit = True
        elif event == Field.Event.POISON:
            self.snake.poison()
            self.score -= 30

            if self.snake.is_dead():
                self.user_exit = True
        elif event == Field.Event.FOOD:
            self.snake.eat()
            self.score += 10

        if self.snake.crash(new_position):
            self.user_exit = True

    def show_end_view(self, screen):
        """ Displays the end game screen and handles user input. """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pylint: disable=no-member
                self.user_quit, self.game_on = True, False
            if event.type == pygame.KEYDOWN:  # pylint: disable=no-member
                if event.key == pygame.K_q:  # pylint: disable=no-member
                    self.user_quit, self.game_on = True, False
                elif event.key == pygame.K_SPACE:  # pylint: disable=no-member
                    self.user_quit = True

        views.end_view(screen, self.score)
        pygame.display.flip()

    def reset_members(self):
        """ Resets memeber variables values to the default ones. """
        self.score, self.user_exit, self.user_quit = 0, False, False
        self.snake = Snake()
        self.field = Field()

    def run(self):
        """ Runs the game. """
        pygame.init()  # pylint: disable=no-member

        screen = pygame.display.set_mode(consts.WINDOW_SIZE)  # pylint: disable=no-member
        pygame.display.set_caption("Adventures of a small Python")
        clock = pygame.time.Clock()

        while self.game_on:
            self.reset_members()
            while not self.user_start:
                self.show_start_view(screen)
                clock.tick(consts.TICKS_PER_MIN)

            while not self.user_exit:
                self.show_game_view(screen)
                clock.tick(consts.TICKS_PER_MIN)

            while not self.user_quit:
                self.show_end_view(screen)
                clock.tick(consts.TICKS_PER_MIN)

        pygame.quit()  # pylint: disable=no-member
