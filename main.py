# Example file showing a basic pygame "game loop"
import pygame, file_manager
import pygame.draw_py

# screen
DISPLAY_WIDTH = 640
DISPLAY_HEIGHT = 360
DEFAULT_IMAGE_SIZE = 16
IMAGE_SIZE_MULTIPLIER = 2*DEFAULT_IMAGE_SIZE

# pygame setup
pygame.init()
SCREEN = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
CLOCK = pygame.time.Clock()
RUNNING = True
DELTA_TIME = 0

GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))

# player stuff
PLAYER_IMAGE = pygame.image.load(file_manager.playerAsset('idle'), "player-idle")
PLAYER_POSITION = pygame.Vector2(SCREEN.get_width() / 2, SCREEN.get_height() / 2)
PLAYER_MOVEMENT_SPEED = 150

while RUNNING:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    # fill the SCREEN with a color to wipe away anything from last frame
    SCREEN.fill("black")

    GAME_DISPLAY.blit(pygame.transform.scale(PLAYER_IMAGE, (IMAGE_SIZE_MULTIPLIER, IMAGE_SIZE_MULTIPLIER)), PLAYER_POSITION)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        PLAYER_POSITION.y -= PLAYER_MOVEMENT_SPEED * DELTA_TIME
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        PLAYER_POSITION.y += PLAYER_MOVEMENT_SPEED * DELTA_TIME
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        PLAYER_POSITION.x -= PLAYER_MOVEMENT_SPEED * DELTA_TIME
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        PLAYER_POSITION.x += PLAYER_MOVEMENT_SPEED * DELTA_TIME

    # flip() the display to put your work on SCREEN
    pygame.display.flip()

    # limits FPS to 60
    # DELTA_TIME is delta time in seconds since last frame, used for framerate-
    # independent physics.
    DELTA_TIME = CLOCK.tick(60) / 1000

pygame.quit()