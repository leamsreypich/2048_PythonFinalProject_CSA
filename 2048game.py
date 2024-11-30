import pygame
import random
import math
from database import initialize_database, get_highest_score, update_highest_score

# Initialize Pygame and the mixer
pygame.init()
pygame.mixer.init()

FPS = 60

WIDTH, HEIGHT = 800, 800
ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS


OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (196, 236, 255)
FONT_COLOR = (85, 107, 47)
OUTLINE_COLOR = (233, 248, 255)

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOVE_VEL = 20

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")


class Tile:
    COLORS = [
        (198, 255, 198),  # Very Pale Green (2)
        (152, 255, 152),  # Light Mint Green (4)
        (175, 238, 238),  # Pale Aqua Blue (8)
        (135, 206, 250),  # Soft Sky Blue (16)
        (176, 224, 230),  # Powder Blue (32)
        (144, 238, 144),  # Light Pastel Teal (64)
        (144, 255, 204),  # Light Seafoam Green (128)
        (230, 230, 250),  # Soft Lavender Blue (256)
        (204, 255, 255),  # Soft Light Cyan (512)
        (204, 204, 255),  # Light Periwinkle Blue (1024)
        (188, 224, 224),  # Muted Teal (2048)
    ]

    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT

    def get_color(self):
        color_index = int(math.log2(self.value)) - 1
        color = self.COLORS[color_index]
        return color

    def draw(self, window):
        color = self.get_color()
        pygame.draw.rect(window, color, (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))

        text = FONT.render(str(self.value), 1, FONT_COLOR)
        window.blit(
            text,
            (
                self.x + (RECT_WIDTH / 2 - text.get_width() / 2),
                self.y + (RECT_HEIGHT / 2 - text.get_height() / 2),
            ),
        )

    def set_pos(self, ceil=False):
        if ceil:
            self.row = math.ceil(self.y / RECT_HEIGHT)
            self.col = math.ceil(self.x / RECT_WIDTH)
        else:
            self.row = math.floor(self.y / RECT_HEIGHT)
            self.col = math.floor(self.x / RECT_WIDTH)

    def move(self, delta):
        self.x += delta[0]
        self.y += delta[1]


# Load the background image
background_image = pygame.image.load("start_screen_background.jpg")  
background_image = pygame.transform.scale(background_image, (800, 800)) 
# Load the sound effect
start_sound = pygame.mixer.Sound("sound_effect.wav")  
start_sound.set_volume(0.8)  # Optional: Set the volume (0.0 to 1.0)
# Load the game-over sound
game_over_sound = pygame.mixer.Sound("game_over_sound.wav")
game_over_sound.set_volume(0.7)  # Adjust the volume


def draw_start_screen(window):
    """
    Draws the start screen with a button to begin the game.
    """
    window.blit(background_image, (0, 0))

    # Draw title text
    title_font = pygame.font.SysFont("comicsans", 80, bold=True)
    title_text = title_font.render("2048 Game", True, FONT_COLOR)
    window.blit(
        title_text,
        (
            WIDTH // 2 - title_text.get_width() // 2,
            HEIGHT // 4 - title_text.get_height() // 2,
        ),
    )

    # Draw start button
    button_width = 200
    button_height = 80
    button_x = WIDTH // 2 - button_width // 2
    button_y = HEIGHT // 2 - button_height // 2
    button_color = (115, 212, 115)
    pygame.draw.rect(window, button_color, (button_x, button_y, button_width, button_height), border_radius=10)

    # Draw button text
    button_font = pygame.font.SysFont("comicsans", 40)
    button_text = button_font.render("Start", True, (255, 255, 255))
    window.blit(
        button_text,
        (
            button_x + (button_width // 2 - button_text.get_width() // 2),
            button_y + (button_height // 2 - button_text.get_height() // 2),
        ),
    )

    pygame.display.update()
    return button_x, button_y, button_width, button_height

def start_screen(window):
    """
    Handles the logic for the start screen.
    Waits for the user to click the start button.
    """
    clock = pygame.time.Clock()

    def draw_content(window):
        draw_start_screen(window)  # Draw the start screen content

    # Apply the fade-in effect 
    fade_in(window, draw_content, duration=7000)

    while True:
        clock.tick(FPS)

        button_x, button_y, button_width, button_height = draw_start_screen(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # Check if the start button is clicked
                if (
                    button_x <= mouse_x <= button_x + button_width
                    and button_y <= mouse_y <= button_y + button_height
                ):
                    start_sound.play()  # Play the sound effect
                    pygame.time.delay(500)  # Pause briefly after the click
                    loading_screen(window)
                    return
                
def fade_in(window, content_function, duration=2000):
    """
    Creates a smooth fade-in effect for the given content.
    :param window: The pygame window.
    :param content_function: A function to draw the content to be faded in.
    :param duration: Duration of the fade-in effect in milliseconds.
    """
    clock = pygame.time.Clock()
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.fill((0, 0, 0))  # Black overlay
    alpha = 255  # Start fully opaque
    fade_step = 255 / (duration / FPS)  # Smooth fade step based on FPS and duration

    while alpha > 0:
        clock.tick(FPS)

        # Draw the main content
        content_function(window)

        # Apply the fade effect
        overlay.set_alpha(alpha)
        window.blit(overlay, (0, 0))

        pygame.display.update()
        alpha -= fade_step  # Reduce alpha gradually
        alpha = max(alpha, 0)  # Ensure alpha doesn't go below 0


def loading_screen(window):
    """
    Displays a loading animation with three dots on top of the start-screen background.
    """
    clock = pygame.time.Clock()
    loading_font = pygame.font.SysFont("comicsans", 50, bold=True)

    # Number of animation frames
    total_frames = 180  # Adjust for the total duration (60 FPS = 3 seconds)
    frames_per_dot = 30  # Frames per dot appearing/disappearing

    for frame in range(total_frames):
        window.blit(background_image, (0, 0))  # Display the start-screen background

        # Create the "Loading" text
        loading_text = loading_font.render("Loading", True, FONT_COLOR)
        window.blit(
            loading_text,
            (
                WIDTH // 2 - loading_text.get_width() // 2,
                HEIGHT // 2 - 100,
            ),
        )

        # Add dots based on the current frame
        num_dots = (frame // frames_per_dot) % 4  # Cycle through 0, 1, 2, 3 dots
        dots_text = loading_font.render("." * num_dots, True, FONT_COLOR)
        window.blit(
            dots_text,
            (
                WIDTH // 2 + loading_text.get_width() // 2,
                HEIGHT // 2 - 100,
            ),
        )

        pygame.display.update()
        clock.tick(FPS)

def draw_grid(window):
    for row in range(1, ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)

    for col in range(1, COLS):
        x = col * RECT_WIDTH
        pygame.draw.line(window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)

    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)


def draw(window, tiles):
    window.fill(BACKGROUND_COLOR)

    for tile in tiles.values():
        tile.draw(window)

    draw_grid(window)

    pygame.display.update()


def get_random_pos(tiles):
    row = None
    col = None
    while True:
        row = random.randrange(0, ROWS)
        col = random.randrange(0, COLS)

        if f"{row}{col}" not in tiles:
            break

    return row, col


def move_tiles(window, tiles, clock, direction):
    updated = True
    blocks = set()

    if direction == "left":
        sort_func = lambda x: x.col
        reverse = False
        delta = (-MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col - 1}")
        merge_check = lambda tile, next_tile: tile.x > next_tile.x + MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.x > next_tile.x + RECT_WIDTH + MOVE_VEL
        )
        ceil = True
    elif direction == "right":
        sort_func = lambda x: x.col
        reverse = True
        delta = (MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == COLS - 1
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col + 1}")
        merge_check = lambda tile, next_tile: tile.x < next_tile.x - MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.x + RECT_WIDTH + MOVE_VEL < next_tile.x
        )
        ceil = False
    elif direction == "up":
        sort_func = lambda x: x.row
        reverse = False
        delta = (0, -MOVE_VEL)
        boundary_check = lambda tile: tile.row == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row - 1}{tile.col}")
        merge_check = lambda tile, next_tile: tile.y > next_tile.y + MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.y > next_tile.y + RECT_HEIGHT + MOVE_VEL
        )
        ceil = True
    elif direction == "down":
        sort_func = lambda x: x.row
        reverse = True
        delta = (0, MOVE_VEL)
        boundary_check = lambda tile: tile.row == ROWS - 1
        get_next_tile = lambda tile: tiles.get(f"{tile.row + 1}{tile.col}")
        merge_check = lambda tile, next_tile: tile.y < next_tile.y - MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.y + RECT_HEIGHT + MOVE_VEL < next_tile.y
        )
        ceil = False

    while updated:
        clock.tick(FPS)
        updated = False
        sorted_tiles = sorted(tiles.values(), key=sort_func, reverse=reverse)

        for i, tile in enumerate(sorted_tiles):
            if boundary_check(tile):
                continue

            next_tile = get_next_tile(tile)
            if not next_tile:
                tile.move(delta)
            elif (
                tile.value == next_tile.value
                and tile not in blocks
                and next_tile not in blocks
            ):
                if merge_check(tile, next_tile):
                    tile.move(delta)
                else:
                    next_tile.value *= 2
                    sorted_tiles.pop(i)
                    blocks.add(next_tile)
            elif move_check(tile, next_tile):
                tile.move(delta)
            else:
                continue

            tile.set_pos(ceil)
            updated = True

        update_tiles(window, tiles, sorted_tiles)

    return end_move(tiles)


def is_game_over(tiles):
    if len(tiles) < ROWS * COLS:
        return False

    for tile in tiles.values():
        adjacent_positions = [
            (tile.row, tile.col - 1),
            (tile.row, tile.col + 1),
            (tile.row - 1, tile.col),
            (tile.row + 1, tile.col),
        ]
        for row, col in adjacent_positions:
            adjacent_tile = tiles.get(f"{row}{col}")
            if adjacent_tile and adjacent_tile.value == tile.value:
                return False

    return True


def display_game_over(window, highest_score, current_score):
    """
    Displays the game-over screen with the highest and current scores.
    """
    pygame.mixer.music.fadeout(1100)
    pygame.time.delay(900)
    game_over_sound.play()

    game_over_font = pygame.font.SysFont("comicsans", 80, bold=True)
    score_font = pygame.font.SysFont("comicsans", 50, bold=True)

    # Render texts
    text = game_over_font.render("Game Over!", True, FONT_COLOR)
    current_score_text = score_font.render(f"Current Score: {current_score}", True, FONT_COLOR)
    score_text = score_font.render(f"Highest Score: {highest_score}", True, FONT_COLOR)

    window.blit(background_image, (0, 0))

    alpha = 0
    fade_speed = 5

    # Convert surfaces for fade-in effect
    text_surface = text.convert_alpha()
    current_score_surface = current_score_text.convert_alpha()
    score_surface = score_text.convert_alpha()

    while alpha < 255:
        text_surface.set_alpha(alpha)
        current_score_surface.set_alpha(alpha)
        score_surface.set_alpha(alpha)

        # Display "Game Over!" text
        window.blit(
            text_surface,
            (
                WIDTH // 2 - text_surface.get_width() // 2,
                HEIGHT // 3 - text_surface.get_height() // 2,
            ),
        )

        # Display current score
        window.blit(
            current_score_surface,
            (
                WIDTH // 2 - current_score_surface.get_width() // 2,
                HEIGHT // 2 - 50,
            ),
        )

        # Display highest score
        window.blit(
            score_surface,
            (
                WIDTH // 2 - score_surface.get_width() // 2,
                HEIGHT // 2 + 50,
            ),
        )

        pygame.display.update()
        pygame.time.delay(50)
        alpha += fade_speed

    # Draw retry button
    button_width, button_height = 200, 80
    button_x, button_y = WIDTH // 2 - button_width // 2, HEIGHT // 2 + 150
    button_color = (115, 212, 115)
    pygame.draw.rect(window, button_color, (button_x, button_y, button_width, button_height), border_radius=10)

    button_font = pygame.font.SysFont("comicsans", 40)
    button_text = button_font.render("Retry", True, (255, 255, 255))
    window.blit(
        button_text,
        (
            button_x + (button_width // 2 - button_text.get_width() // 2),
            button_y + (button_height // 2 - button_text.get_height() // 2),
        ),
    )

    pygame.display.update()

    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if (
                    button_x <= mouse_x <= button_x + button_width
                    and button_y <= mouse_y <= button_y + button_height
                ):
                    start_sound.play()
                    return "retry"






def end_move(tiles):
    if len(tiles) == 16:
        return "lost"

    row, col = get_random_pos(tiles)
    tiles[f"{row}{col}"] = Tile(random.choice([2, 4]), row, col)
    return "continue"


def update_tiles(window, tiles, sorted_tiles):
    tiles.clear()
    for tile in sorted_tiles:
        tiles[f"{tile.row}{tile.col}"] = tile

    draw(window, tiles)


def generate_tiles():
    tiles = {}
    for _ in range(2):
        row, col = get_random_pos(tiles)
        tiles[f"{row}{col}"] = Tile(2, row, col)

    return tiles





def main(window):
    initialize_database()  # Initialize the database

    while True:  # Game loop
        pygame.mixer.music.stop()
        pygame.mixer.music.load("Backgroundmusic.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

        start_screen(window)
        tiles = generate_tiles()
        player_highest_score = get_highest_score()  # Fetch the current highest score

        run = True
        while run:
            clock = pygame.time.Clock()
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        move_tiles(window, tiles, clock, "left")
                    if event.key == pygame.K_RIGHT:
                        move_tiles(window, tiles, clock, "right")
                    if event.key == pygame.K_UP:
                        move_tiles(window, tiles, clock, "up")
                    if event.key == pygame.K_DOWN:
                        move_tiles(window, tiles, clock, "down")

            if is_game_over(tiles):
                max_tile = max(tile.value for tile in tiles.values())  # Get the max tile value
                if max_tile > player_highest_score:
                    update_highest_score(max_tile)  # Update the database if a new high score is achieved
                    player_highest_score = max_tile  # Update the local highest score

                result = display_game_over(window, player_highest_score, max(tile.value for tile in tiles.values()))
                if result == "retry":
                    run = False
                else:
                    pygame.quit()
                    exit()

            draw(window, tiles)





if __name__ == "__main__":
    main(WINDOW)
