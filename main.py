import pygame
import player
from constants import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    p1 = player.player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    updatable.add(p1)
    drawable.add(p1)
    while True:
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        for s in drawable:
            s.draw(screen)
        updatable.update(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()