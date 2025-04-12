import pygame

from circleshape import CircleShape
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2
        return pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)