import pygame
import random

# Initialize Pygame
pygame.init()

# Set the size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create the players
player1 = pygame.Rect(50, 50, 50, 50)
player2 = pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100, 50, 50)

# Define the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set the initial velocity of the players
player1_vel = (5, 0)
player2_vel = (0, 0)

# Set the clock
clock = pygame.time.Clock()

# Set the bot direction
bot_direction = 0

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player2_vel = (-5, 0)
            elif event.key == pygame.K_RIGHT:
                player2_vel = (5, 0)
            elif event.key == pygame.K_UP:
                player2_vel = (0, -5)
            elif event.key == pygame.K_DOWN:
                player2_vel = (0, 5)

    # Move player 1
    if bot_direction == 0:
        player1_vel = (5, 0)
        if player1.right >= SCREEN_WIDTH:
            bot_direction = 1
    elif bot_direction == 1:
        player1_vel = (0, 5)
        if player1.bottom >= SCREEN_HEIGHT:
            bot_direction = 2
    elif bot_direction == 2:
        player1_vel = (-5, 0)
        if player1.left <= 0:
            bot_direction = 3
    elif bot_direction == 3:
        player1_vel = (0, -5)
        if player1.top <= 0:
            bot_direction = 0
    player1.move_ip(player1_vel)

    # Move player 2
    player2.move_ip(player2_vel)

    # Check if the players collide
    if player1.colliderect(player2):
        print("Player 1 caught player 2!")
        running = False

    # Draw the players and the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, player1)
    pygame.draw.rect(screen, BLACK, player2)
    pygame.display.flip()

    # Set the FPS
    clock.tick(60)

# Quit the game
pygame.quit()
