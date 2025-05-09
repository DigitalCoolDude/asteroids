import pygame

from circleshape import CircleShape
# from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SPEED, PLAYER_TURN_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt