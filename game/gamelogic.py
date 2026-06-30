import pygame as pyg
import random as rand

# Game Logic


# Difficulty settings, (easy is default)
# Change in code from "easy", "medium", "hard"
select_diff = "medium"

if select_diff == "easy":
    gravity = 0.5
    jump_vel = -7.5
    tower_gap = 200
    tower_spawn_interval = 150
elif select_diff == "medium":
    gravity = 0.75
    jump_vel = -10
    tower_gap = 180
    tower_spawn_interval = 120
else:
    gravity = 1
    jump_vel = -12.5
    tower_gap = 160
    tower_spawn_interval = 90


# Constants
# Screen
SCREEN_HEIGHT = 750
SCREEN_WIDTH = 750

# Sprite
GRAVITY = gravity
SPRITE_START_X = 100
SPRITE_START_Y = 300
JUMP_VEL = jump_vel

# Tower
MIN_TOWER_HEIGHT = 50
TOWER_WIDTH = 50
TOWER_GAP = tower_gap
TOWER_SPEED = 3
TOWER_SPAWN_INTERVAL = tower_spawn_interval  # (frames)


class Square:
    """Main player sprite, loaded from an image of a square character."""

    def __init__(self):
        """Initialise the square sprite."""
        self.x_pos = SPRITE_START_X
        self.y_pos = SPRITE_START_Y
        self.vertical_vel = 0
        self.image = pyg.image.load("images/sprite.png")

    def apply_gravity(self):
        """Update the square's y position based on a gravity variable"""

        self.vertical_vel += GRAVITY
        self.y_pos += self.vertical_vel

    def apply_jump(self):
        """Update the square's velocity"""
        self.vertical_vel = JUMP_VEL
        self.y_pos += self.vertical_vel

    def draw_to_screen(self, screen):
        """Draw the square sprite to the screen."""
        screen.blit(self.image, (self.x_pos, self.y_pos))


class Tower_object:

    def __init__(self):
        self.x_pos = SCREEN_WIDTH
        self.height = rand.randint(
            MIN_TOWER_HEIGHT,
            (SCREEN_HEIGHT - TOWER_GAP - MIN_TOWER_HEIGHT),
        )
        self.y_pos = SCREEN_HEIGHT - self.height
        self.top_height = self.y_pos - TOWER_GAP

    def spawn_tower(self, screen):
        # bottom tower
        pyg.draw.rect(
            screen,
            (0, 200, 180),
            (int(self.x_pos), self.y_pos, TOWER_WIDTH, self.height),
        )

        # top tower
        pyg.draw.rect(
            screen, (0, 200, 180), (int(self.x_pos), 0, TOWER_WIDTH, self.top_height)
        )

    def move_tower(self):
        self.x_pos -= TOWER_SPEED


# Collisions
# ==========================


def collides(square, tower):
    """Returns true if the sprite collides with a tower, else return false"""

    # Create hitboxes for sprite and tower sections.
    sprite_rect = pyg.Rect(
        square.x_pos, square.y_pos, square.image.get_width(), square.image.get_height()
    )

    bottom_rect = pyg.Rect(tower.x_pos, tower.y_pos, TOWER_WIDTH, tower.height)
    top_rect = pyg.Rect(tower.x_pos, 0, TOWER_WIDTH, tower.top_height)

    # Check if there are any collisions, return True or False.
    return sprite_rect.colliderect(bottom_rect) or sprite_rect.colliderect(top_rect)


def score_counter(square, towers, score):

    for tower in towers:
        if not tower[1]:

            if (tower[0].x_pos) + TOWER_WIDTH < square.x_pos:
                score += 1
                tower[1] = True
    return score
