# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from circleshape import CircleShape
from player import Player

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

    # Initalize player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y, PLAYER_RADIUS)

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

        # Draw a solid blue circle in the center
        # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

        # Player object
        player.draw(screen)

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit
    pygame.quit()

if __name__ == "__main__":
    main()