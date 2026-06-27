import pygame as pyg
import gamelogic as gl

square = gl.Square()


# Initialise Pygame, initialise the display as SCREEN, set the game title.
pyg.init()
pyg.display.set_allow_screensaver(False)
SCREEN = pyg.display.set_mode((gl.SCREEN_WIDTH, gl.SCREEN_HEIGHT), pyg.SCALED, vsync=1)
pyg.display.set_caption("Flappy Square")


# Create an empty towers list, set the frame count to 0, create the clock.
# Set the game as active, create the high score variables.
towers = []
frame_count = 0
clock = pyg.time.Clock()
game_active = True
high_score = 0


# Fonts
score_font = pyg.font.SysFont(None, 36)  # live score
hud_font = pyg.font.SysFont(None, 26)  # high score + reset hint
gameover_font = pyg.font.SysFont(None, 50)  # game over screen


# Main game loop
running = True
while running:

    for event in pyg.event.get():
        # Quit game window if built in X button clicked.
        if event.type == pyg.QUIT:
            running = False

        if event.type == pyg.KEYDOWN:

            # Apply jump to the sprite if space or up arrow clicked and the game is active.
            if event.key == pyg.K_SPACE or event.key == pyg.K_UP:
                if game_active:
                    square.apply_jump()

            # Reset the game
            elif event.key == pyg.K_s:
                gl.score = 0
                frame_count = 0
                towers = []
                square = gl.Square()
                game_active = True

    if game_active:
        SCREEN.fill((15, 15, 35))

        # Add a new tower to the list of towers.
        if frame_count % gl.TOWER_SPAWN_INTERVAL == 0:
            towers.append([gl.Tower_object(), False])
        # draw every tower in the tower list at the new position.
        # if a tower has moved all the way left remove it.
        for tower in towers:
            tower[0].move_tower()
            tower[0].spawn_tower(SCREEN)

        if towers[0][0].x_pos <= -gl.TOWER_WIDTH:
            towers.remove(towers[0])

        # Apply gravity and draw the square.
        square.apply_gravity()
        square.draw_to_screen(SCREEN)

        # Update and display score + info:
        score = gl.score_counter(square, towers)
        text1 = score_font.render(f"Score: {score}", True, (255, 0, 0))

        # If score => high score, use the current score as the display text and change color.
        if gl.score >= high_score:
            color = (255, 0, 0)
            high_score = gl.score
        else:
            color = (255, 255, 255)

        text2 = hud_font.render(f"High Score = {high_score}", True, color)
        text3 = hud_font.render("Press s to reset", True, (255, 255, 255))

        SCREEN.blit(text1, (10, 10))
        SCREEN.blit(text2, (gl.SCREEN_WIDTH - 150, 10))
        SCREEN.blit(text3, (gl.SCREEN_WIDTH - 150, 30))

        # Check for collisions
        # -> Checks all towers in case tower speed/width is adjusted later,
        # -> basically no complexity trade off since only 3-5 towers loaded at once.
        # Note: towers will never be empty as a tower is spawned at frame count = 0.
        if (
            any(gl.collides(square, t[0]) for t in towers)
            or 0 > square.y_pos
            or square.y_pos > gl.SCREEN_HEIGHT
        ):
            game_active = False

        frame_count += 1

    # Game over screen (Click s to reset).
    else:
        SCREEN.fill((15, 15, 35))

        text = gameover_font.render(f"GAME OVER - SCORE: {score}", True, (255, 0, 0))

        text2 = gameover_font.render(f"HIGH SCORE: {high_score}", True, (0, 200, 180))

        if high_score <= score:
            if score != 0:
                text2 = gameover_font.render(
                    f"NEW HIGH SCORE: {high_score}", True, (0, 200, 180)
                )

        text3 = gameover_font.render("Press s to reset", True, (255, 255, 255))

        text_rect = text.get_rect(
            center=(gl.SCREEN_WIDTH // 2, (gl.SCREEN_HEIGHT // 2) - 50)
        )
        text_rect2 = text2.get_rect(
            center=(gl.SCREEN_WIDTH // 2, gl.SCREEN_HEIGHT // 2)
        )
        text_rect3 = text3.get_rect(
            center=(gl.SCREEN_WIDTH // 2, (gl.SCREEN_HEIGHT // 2) + 50)
        )
        SCREEN.blit(text, text_rect)
        SCREEN.blit(text2, text_rect2)
        SCREEN.blit(text3, text_rect3)

    clock.tick(60)
    pyg.display.flip()


# Quit the game
pyg.quit()
