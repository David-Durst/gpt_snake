import random

# Constants
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Function to calculate distance between two points
def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Snake bot class
class SnakeBot:
    def __init__(self):
        self.direction = None

    # Method to get the next move
    def get_move(self, snake_head, food_position, obstacles):
        # If no direction is set, choose a random direction
        if not self.direction:
            self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

        # Calculate distance to the food in each direction
        distances = {
            UP: distance((snake_head[0], snake_head[1]-1), food_position),
            DOWN: distance((snake_head[0], snake_head[1]+1), food_position),
            LEFT: distance((snake_head[0]-1, snake_head[1]), food_position),
            RIGHT: distance((snake_head[0]+1, snake_head[1]), food_position),
        }

        # Sort directions by distance to food
        sorted_directions = sorted(distances.keys(), key=lambda d: distances[d])

        # Choose the first direction that is not blocked by an obstacle
        for direction in sorted_directions:
            next_position = (snake_head[0] + direction[0], snake_head[1] + direction[1])
            if next_position not in obstacles:
                self.direction = direction
                return direction

        # If all directions are blocked, choose a random direction
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        return self.direction