
# ============================================================
#  SNAKE GAME (pygame)
#  WASD keys to move. Eat the food, avoid the rocks!
# ============================================================
import random
import pygame

# ============================================================
#  PART 1: GAME SETTINGS
# ============================================================
GAME_TITLE = "Pink Snake Eater"
CELL_SIZE = 34
GRID_WIDTH = 24
GRID_HEIGHT = 18
SPEED = 10
START_LENGTH = 3
POINTS_PER_FOOD = 1
GROW_PER_FOOD = 1
WALLS_KILL = False

# Pink Theme Colors
BACKGROUND_COLOR = (255, 230, 240)
GRID_COLOR = (255, 200, 220)
SNAKE_COLOR = (255, 105, 180)
HEAD_COLOR = (219, 60, 140)
FOOD_COLOR = (255, 80, 80)
TEXT_COLOR = (100, 40, 70)

# ROCK SETTINGS
ROCK_COLOR = (110, 130, 140)
ROCKS = [(6, 6), (7, 5), (8, 5),
         (15, 12), (16, 12), (17, 12)]

# ============================================================
#  PART 2: SETUP
# ============================================================
pygame.init()
WIDTH = CELL_SIZE * GRID_WIDTH
HEIGHT = CELL_SIZE * GRID_HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)


# ============================================================
#  PART 3: FUNCTIONS
# ============================================================
def new_game():
    """Return a fresh snake, direction, food, score and growth counter."""
    start_x = GRID_WIDTH // 2
    start_y = GRID_HEIGHT // 2
    snake = []

    for i in range(START_LENGTH):
        snake.append((start_x - i, start_y))

    direction = (1, 0)
    food = place_food(snake)

    return snake, direction, food, 0, 0


def place_food(snake):
    """Pick a random empty square for the food."""
    while True:
        spot = (random.randint(0, GRID_WIDTH - 1),
                random.randint(0, GRID_HEIGHT - 1))

        # Food cannot appear on the snake or rocks
        if spot not in snake and spot not in ROCKS:
            return spot


def draw_square(position, color):
    """Draw one grid square."""
    x, y = position
    rect = pygame.Rect(
        x * CELL_SIZE,
        y * CELL_SIZE,
        CELL_SIZE,
        CELL_SIZE
    )
    pygame.draw.rect(screen, color, rect, border_radius=5)


def draw_text(text, y):
    """Draw centered text."""
    image = font.render(text, True, TEXT_COLOR)
    screen.blit(
        image,
        (WIDTH // 2 - image.get_width() // 2, y)
    )


def draw_game(snake, food, score):
    """Draw background, grid, rocks, food, snake and score."""
    screen.fill(BACKGROUND_COLOR)

    # Draw grid lines
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))

    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))

    # Draw the rocks
    for rock in ROCKS:
        draw_square(rock, ROCK_COLOR)

    # Draw food
    draw_square(food, FOOD_COLOR)

    # Draw snake body
    for part in snake[1:]:
        draw_square(part, SNAKE_COLOR)

    # Draw snake head
    draw_square(snake[0], HEAD_COLOR)

    # Draw score
    draw_text("Score: " + str(score), 10)


# ============================================================
#  PART 4: THE GAME LOOP
# ============================================================
snake, direction, food, score, grow = new_game()
game_over = False
running = True

while running:

    # ---- 1. EVENTS: read the keyboard ----
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if game_over:
                if event.key == pygame.K_r:
                    snake, direction, food, score, grow = new_game()
                    game_over = False

                elif event.key == pygame.K_q:
                    running = False

            # WASD Controls
            elif event.key == pygame.K_w and direction != (0, 1):
                direction = (0, -1)

            elif event.key == pygame.K_s and direction != (0, -1):
                direction = (0, 1)

            elif event.key == pygame.K_a and direction != (1, 0):
                direction = (-1, 0)

            elif event.key == pygame.K_d and direction != (-1, 0):
                direction = (1, 0)

    # ---- 2. UPDATE: move the snake and check collisions ----
    if not game_over:

        head_x, head_y = snake[0]
        new_head = (
            head_x + direction[0],
            head_y + direction[1]
        )

        # Wall collision or wall passing
        if WALLS_KILL:
            if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH
                    or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
                game_over = True

        else:
            new_head = (
                new_head[0] % GRID_WIDTH,
                new_head[1] % GRID_HEIGHT
            )

        # Check if snake hits itself or a rock
        if new_head in snake or new_head in ROCKS:
            game_over = True

        if not game_over:

            snake.insert(0, new_head)

            # Check if snake eats food
            if new_head == food:
                score = score + POINTS_PER_FOOD
                grow = grow + GROW_PER_FOOD
                food = place_food(snake)

            # Snake growth
            if grow > 0:
                grow = grow - 1
            else:
                snake.pop()

    # ---- 3. DRAW: paint the new frame ----
    draw_game(snake, food, score)

    if game_over:
        draw_text("GAME OVER", HEIGHT // 2 - 40)
        draw_text(
            "Score: " + str(score) + "   R = play again   Q = quit",
            HEIGHT // 2
        )

    pygame.display.flip()
    clock.tick(SPEED)

pygame.quit()
