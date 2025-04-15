# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize the pygame library
    pygame.init()

    # Create an object to help track time
    game_clock = pygame.time.Clock()

    # Initalize change in time var
    dt = 0

    # Set up the drawing window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteriods = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteriods, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)
    
    # Initalize player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    player = Player(x, y, PLAYER_RADIUS)
    asteriodsfield = AsteroidField()

    # Run until the user asks to quit
    running = True
    while running:

        # Change in time
        dt = game_clock.tick(60)/1000

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((0,0,0))
        
        updatable.update(dt)
        
        for sprite in drawable:
            sprite.draw(screen)     

        for sprite in asteriods:
            if sprite.collide(player):   
                print("Game over!")
                sys.exit()

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit
    pygame.quit()

if __name__ == "__main__":
    main()