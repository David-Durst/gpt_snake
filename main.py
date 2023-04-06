import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Two Player Snake Game")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the font for displaying the score
font = pygame.font.SysFont("Arial", 24)

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set up the game variables
player1_x = window_width // 4
player1_y = window_height // 2
player1_direction = "right"
player1_score = 0
player1_snake = [(player1_x, player1_y)]
player2_x = window_width // 4 * 3
player2_y = window_height // 2
player2_direction = "left"
player2_score = 0
player2_snake = [(player2_x, player2_y)]
food_x = random.randint(0, window_width // 20 - 1) * 20
food_y = random.randint(0, window_height // 20 - 1) * 20

# Set up the game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and player1_direction != "down":
                player1_direction = "up"
            elif event.key == pygame.K_a and player1_direction != "right":
                player1_direction = "left"
            elif event.key == pygame.K_s and player1_direction != "up":
                player1_direction = "down"
            elif event.key == pygame.K_d and player1_direction != "left":
                player1_direction = "right"
            elif event.key == pygame.K_UP and player2_direction != "down":
                player2_direction = "up"
            elif event.key == pygame.K_LEFT and player2_direction != "right":
                player2_direction = "left"
            elif event.key == pygame.K_DOWN and player2_direction != "up":
                player2_direction = "down"
            elif event.key == pygame.K_RIGHT and player2_direction != "left":
                player2_direction = "right"

    # Update the game state
    if player1_direction == "up":
        player1_y -= 20
    elif player1_direction == "left":
        player1_x -= 20
    elif player1_direction == "down":
        player1_y += 20
    elif player1_direction == "right":
        player1_x += 20
    player1_snake.insert(0, (player1_x, player1_y))
    if player1_x < 0 or player1_x >= window_width or player1_y < 0 or player1_y >= window_height or (player1_x, player1_y) in player2_snake or len(player1_snake) > player1_score + 2:
        game_over = True
    if player1_x == food_x and player1_y == food_y:
        player1_score += 1
        food_x = random.randint(0, window_width // 20 - 1) * 20
        food_y = random.randint(0, window_height // 20 - 1) * 20
    else:
        player1_snake.pop()

    if player2_direction == "up":
        player2_y -= 20
    elif player2_direction == "left":
        player2_x -= 20
    elif player2_direction == "down":
        player2_y += 20
    elif player2_direction == "right":
        player2_x += 20
    player2_snake.insert(0, (player2_x, player2_y))
    if player2_x < 0 or player2_x >= window_width or player2_y < 0 or player2_y >= window_height or (player2_x, player2_y) in player1_snake or len(player2_snake) > player2_score + 2:
        game_over = True
    if player2_x == food_x and player2_y == food_y:
        player2_score += 1
        food_x = random.randint(0, window_width // 20 - 1) * 20
        food_y = random.randint(0, window_height // 20 - 1) * 20
    else:
        player2_snake.pop()

    # Draw the game objects
    window.fill(white)
    pygame.draw.rect(window, green, (food_x, food_y, 20, 20))
    for x, y in player1_snake:
        pygame.draw.rect(window, black, (x, y, 20, 20))
    for x, y in player2_snake:
        pygame.draw.rect(window, red, (x, y, 20, 20))
    player1_score_text = font.render("Player 1 Score: " + str(player1_score), True, black)
    window.blit(player1_score_text, (10, 10))
    player2_score_text = font.render("Player 2 Score: " + str(player2_score), True, black)
    window.blit(player2_score_text, (window_width - player2_score_text.get_width() - 10, 10))
    pygame.display.update()

    # Delay the game loop to achieve a constant frame rate
    clock.tick(10)
