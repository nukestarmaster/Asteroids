import pygame
import player
import asteroid
import asteroidfield
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    p1 = player.player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    ast_field = asteroidfield.AsteroidField()
    while True:
        screen.fill("black")
        updatable.update(dt)
        for a in asteroids:
            if p1.collide(a):
                print('Game Over')
                return
        for s in drawable:
            s.draw(screen)
        dt = clock.tick(60) / 1000
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()