import math

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
def bot_avoid_opponent(player1, player2):
    # Calculate the distance between the two players
    distance = math.sqrt((player1.x - player2.x) ** 2 + (player1.y - player2.y) ** 2)

    # If the opponent is too close, move away from them
    if distance < 100:
        dx = player1.x - player2.x
        dy = player1.y - player2.y
        angle = math.atan2(dy, dx)
        new_x = player1.x + math.cos(angle) * 5
        new_y = player1.y + math.sin(angle) * 5
        return pygame.Rect(new_x, new_y, player1.width, player1.height)

    # Otherwise, move randomly
    dx = random.choice([-5, 5])
    dy = random.choice([-5, 5])
    new_x = player1.x + dx
    new_y = player1.y + dy
    return pygame.Rect(new_x, new_y, player1.width, player1.height)


import math


def maximize_distance_bot(player_rect, opponent_rect, screen_width, screen_height, speed):
    # Compute the center points of the player and opponent rectangles
    player_center = player_rect.center
    opponent_center = opponent_rect.center

    # Compute the distance between the player and opponent centers
    dx = player_center[0] - opponent_center[0]
    dy = player_center[1] - opponent_center[1]
    distance = math.sqrt(dx ** 2 + dy ** 2)

    # Compute the maximum possible distance between the player and opponent
    max_distance = math.sqrt(screen_width ** 2 + screen_height ** 2)

    # If the player is already far away from the opponent, don't move
    if distance >= max_distance / 2:
        return player_rect

    # Compute the direction vector from the player to the opponent
    direction = (dx / distance, dy / distance)

    # Compute the new position of the player by moving in the opposite direction
    delta_x = direction[0] * -speed
    delta_y = direction[1] * -speed
    new_x = player_rect.left + delta_x
    new_y = player_rect.top + delta_y

    # Wrap around the player if they run off the edge of the screen
    if new_x < 0:
        new_x = screen_width - player_rect.width
    elif new_x > screen_width - player_rect.width:
        new_x = 0
    if new_y < 0:
        new_y = screen_height - player_rect.height
    elif new_y > screen_height - player_rect.height:
        new_y = 0

    return pygame.Rect(new_x, new_y, player_rect.width, player_rect.height)

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

    # Move player 2
    player2.move_ip(player2_vel)

    # Move player 1
    player1 = bot_avoid_opponent(player1, player2)
    #player1 = maximize_distance_bot(player1, player2, SCREEN_WIDTH, SCREEN_HEIGHT, 5)

    # Check if the players collide
    if player1.colliderect(player2):
        print("Player 1 caught player 2!")
        running = False

    # Wrap around the players if they go off the edge of the screen
    if player1.left > SCREEN_WIDTH:
        player1.left = 0 - player1.width
    elif player1.right < 0:
        player1.right = SCREEN_WIDTH + player1.width
    if player1.top > SCREEN_HEIGHT:
        player1.top = 0 - player1.height
    elif player1.bottom < 0:
        player1.bottom = SCREEN_HEIGHT + player1.height

    if player2.left > SCREEN_WIDTH:
        player2.left = 0 - player2.width
    elif player2.right < 0:
        player2.right = SCREEN_WIDTH + player2.width
    if player2.top > SCREEN_HEIGHT:
        player2.top = 0 - player2.height
    elif player2.bottom < 0:
        player2.bottom = SCREEN_HEIGHT + player2.height

    # Draw the players and the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, player1)
    pygame.draw.rect(screen, BLACK, player2)
    pygame.display.flip()

    # Set the FPS
    clock.tick(60)

# Quit the game
pygame.quit()

