
import circleshape
import pygame
import shot
from constants import *

class player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
        player.containers = (updatable, drawable)
        updatable.add(self)
        drawable.add(self)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def accelerate(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * PLAYER_ACCELERATION * dt

    def update(self, dt):
        self.position += self.velocity * dt
        self.velocity *= 1 - PLAYER_FRICTION * dt
        self.cooldown -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.accelerate(dt)
        if keys[pygame.K_s]:
            self.accelerate(-dt)
        if keys[pygame.K_SPACE]:
            if self.cooldown <= 0:
                self.shoot()
                self.cooldown = PLAYER_SHOOT_COOLDOWN

    def shoot(self):
        velocity = pygame.Vector2(0, 1).rotate(self.rotation)*SHOT_SPEED + self.velocity
        new_shot = shot.shot(self.position.x, self.position.y, velocity)