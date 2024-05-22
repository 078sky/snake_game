# Snake Game

import pygame
import sys
import random
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')

    # Clock for controlling the frame rate
    clock = pygame.time.Clock()

    # Font for displaying the score
    font = pygame.font.SysFont('arial', 35)

    # Function to reset the game state
    def reset_game():
        global snake_pos, snake_body, snake_direction, change_to, food_pos, food_spawn, obstacle_pos, score, paused
        snake_pos = [100, 50]
        snake_body = [[100, 50], [90, 50], [80, 50]]
        snake_direction = 'RIGHT'
        change_to = snake_direction
        food_pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
        food_spawn = True
        obstacle_pos = [[random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10] for _ in range(5)]
        score = 0
        paused = False

    # Function to display the score
    def show_score(choice, color, font, size):
        score_surface = font.render('Score: ' + str(score), True, color)
        score_rect = score_surface.get_rect()
        score_rect.midtop = (SCREEN_WIDTH / 2, 15)
        screen.blit(score_surface, score_rect)

    # Function to display the pause message
    def show_pause_message():
        pause_surface = font.render('Game Paused. Press P to Resume.', True, WHITE)
        pause_rect = pause_surface.get_rect()
        pause_rect.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        screen.blit(pause_surface, pause_rect)
        pygame.display.flip()

    # Reset the game state initially
    reset_game()

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                elif event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        show_pause_message()

        if not paused:
            # Validate direction
            if change_to == 'UP' and snake_direction != 'DOWN':
                snake_direction = change_to
            if change_to == 'DOWN' and snake_direction != 'UP':
                snake_direction = change_to
            if change_to == 'LEFT' and snake_direction != 'RIGHT':
                snake_direction = change_to
            if change_to == 'RIGHT' and snake_direction != 'LEFT':
                snake_direction = change_to

            # Move the snake
            if snake_direction == 'UP':
                snake_pos[1] -= 10
            if snake_direction == 'DOWN':
                snake_pos[1] += 10
            if snake_direction == 'LEFT':
                snake_pos[0] -= 10
            if snake_direction == 'RIGHT':
                snake_pos[0] += 10

            # Snake body growing mechanism
            snake_body.insert(0, list(snake_pos))
            if snake_pos == food_pos:
                food_spawn = False
                score += 1
            else:
                snake_body.pop()

            if not food_spawn:
                food_pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
            food_spawn = True

            # Fill the screen with black
            screen.fill(BLACK)

            # Draw the snake
            for pos in snake_body:
                pygame.draw.circle(screen, GREEN, (pos[0] + 5, pos[1] + 5), 5)

            # Draw the food
            pygame.draw.rect(screen, WHITE, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

            # Draw the obstacles
            for pos in obstacle_pos:
                pygame.draw.rect(screen, RED, pygame.Rect(pos[0], pos[1], 10, 10))

            # Check for collision with walls
            if snake_pos[0] < 0 or snake_pos[0] >= SCREEN_WIDTH or snake_pos[1] < 0 or snake_pos[1] >= SCREEN_HEIGHT:
                logging.info('Collision with wall detected.')
                reset_game()

            # Check for collision with self
            for block in snake_body[1:]:
                if snake_pos == block:
                    logging.info('Collision with self detected.')
                    reset_game()

            # Check for collision with obstacles
            for pos in obstacle_pos:
                if snake_pos == pos:
                    logging.info('Collision with obstacle detected.')
                    reset_game()

            # Display the score
            show_score(1, WHITE, font, 35)

            # Update the display
            pygame.display.flip()

        # Cap the frame rate
        clock.tick(15)

except Exception as e:
    logging.error(f'An error occurred: {e}')
finally:
    # Quit Pygame
    pygame.quit()
    logging.info('Game has been quit successfully.')
    logging.info(f'Final Score: {score}')

