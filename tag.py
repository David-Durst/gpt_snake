import math

import pygame
import random

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set the width and height of the screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# Set the speed of the players
PLAYER_SPEED = 5

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the caption of the screen
pygame.display.set_caption("Tag Game")

# Create the players
player1 = pygame.Rect(50, 50, 50, 50)
player2 = pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100, 50, 50)

# Set the starting player
it_player = player1

# Set the game loop variable
done = False

# Set the clock
clock = pygame.time.Clock()

# Set the font
font = pygame.font.Font(None, 36)

# Set the score
player1_score = 0
player2_score = 0

# Game loop
while not done:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        it_player.x -= PLAYER_SPEED
    elif keys[pygame.K_RIGHT]:
        it_player.x += PLAYER_SPEED
    elif keys[pygame.K_UP]:
        it_player.y -= PLAYER_SPEED
    elif keys[pygame.K_DOWN]:
        it_player.y += PLAYER_SPEED

    # Check if the player is out of bounds
    if it_player.x < 0:
        it_player.x = 0
    elif it_player.x > SCREEN_WIDTH - it_player.width:
        it_player.x = SCREEN_WIDTH - it_player.width
    if it_player.y < 0:
        it_player.y = 0
    elif it_player.y > SCREEN_HEIGHT - it_player.height:
        it_player.y = SCREEN_HEIGHT - it_player.height

    # Check if the player is tagged
    if it_player.colliderect(player1) and it_player != player1:
        it_player = player1
        player2_score += 1
    elif it_player.colliderect(player2) and it_player != player2:
        it_player = player2
        player1_score += 1

    # Clear the screen
    screen.fill(WHITE)

    # Draw the players
    pygame.draw.rect(screen, RED, player1)
    pygame.draw.rect(screen, BLUE, player2)

    # Draw the score
    text = font.render("Player 1: " + str(player1_score) + " Player 2: " + str(player2_score), True, BLACK)
    screen.blit(text, [10, 10])

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()

import json

def save_game_state(players, tagged_player, game_time):
    # Create a dictionary to store the game state
    game_state = {"players": players,
                  "tagged_player": tagged_player,
                  "game_time": game_time}

    # Write the game state to a file
    with open("game_state.json", "w") as file:
        json.dump(game_state, file)

def move_towards(rect, target_rect, speed):
    dx = target_rect.centerx - rect.centerx
    dy = target_rect.centery - rect.centery
    dist = math.sqrt(dx ** 2 + dy ** 2)
    if dist != 0:
        dx = dx / dist
        dy = dy / dist
    rect.x += dx * speed
    rect.y += dy * speed

def avoid_opponent(player_rect, opponent_rect):
    """
    Returns a new position for the player rectangle that tries to avoid the opponent rectangle.
    """
    # Determine the direction to move in
    dx = player_rect.centerx - opponent_rect.centerx
    dy = player_rect.centery - opponent_rect.centery
    if dx > 0:
        x_dir = -1
    elif dx < 0:
        x_dir = 1
    else:
        x_dir = 0
    if dy > 0:
        y_dir = -1
    elif dy < 0:
        y_dir = 1
    else:
        y_dir = 0

    # Check if the new position is valid
    new_rect = player_rect.move(x_dir * PLAYER_SPEED, y_dir * PLAYER_SPEED)
    if not new_rect.colliderect(opponent_rect):
        return new_rect

    # Try moving in the other direction
    if x_dir != 0:
        new_rect = player_rect.move(-x_dir * PLAYER_SPEED, 0)
        if not new_rect.colliderect(opponent_rect):
            return new_rect
    if y_dir != 0:
        new_rect = player_rect.move(0, -y_dir * PLAYER_SPEED)
        if not new_rect.colliderect(opponent_rect):
            return new_rect

    # If no valid move found, return current position
    return player_rect

def tag_bot(player_rect, opponent_rect, speed):
    if player_rect.colliderect(opponent_rect):
        return True
    else:
        move_towards(player_rect, opponent_rect, speed)
        return False


