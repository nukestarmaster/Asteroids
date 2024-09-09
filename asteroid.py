import circleshape
import pygame
from constants import *

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        Asteroid.containers = (updatable, drawable, asteroids)
        updatable.add(self)
        drawable.add(self)
        asteroids.add(self)
  
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

