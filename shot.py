import circleshape
from constants import *


class shot(circleshape.CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        shot.containers = (updatable, drawable, shots)
        updatable.add(self)
        drawable.add(self)
        shots.add(self)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
