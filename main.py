import pygame
from constants import *
from player import *

def main():
    print('Start asteroids!')


if __name__ == "__main__":
    #pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)

    #Game loop
    while running:
        # event for exit request
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            player.update(-dt)

        if keys[pygame.K_d]:
            player.update(dt)

        screen.fill('black')
        player.draw(screen)
         # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000
        
    pygame.quit()
            