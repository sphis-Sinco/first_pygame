# Example file showing a basic pygame "game loop"
import pygame, file_manager
import pygame.draw_py

# screen
display_width = 640
display_height = 360

# pygame setup
pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
running = True
dt = 0

gameDisplay = pygame.display.set_mode((display_width,display_height))

# player stuff
playerImg = pygame.image.load(file_manager.playerAsset('idle'), "player-idle")
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    gameDisplay.blit(playerImg, player_pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()