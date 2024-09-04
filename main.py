import pygame
import player
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    p1 = player.player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        screen.fill("black")
        p1.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()