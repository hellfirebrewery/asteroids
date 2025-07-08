import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()

    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2)
   
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill(color='black')

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

       #limits the framerate to 60 FPS
        clk = clock.tick(60)
        dt = clk / 1000

if __name__ == "__main__":
    main()
