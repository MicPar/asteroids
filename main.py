import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    delta_time = 0
    game_over = False
    exit_timer = 3
    
    debris = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Debris.containers = (debris, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    

    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    test_asteroid = Asteroid(0, 0, 10)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        if game_over == True:
            exit_timer -= delta_time
        if exit_timer < 0:
            sys.exit()

        
        #state        
        updatable.update(delta_time)
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                player.impact()
                asteroid.split()
                game_over = True
                #sys.exit()
            for shot in shots:
                if shot.collision_check(asteroid):
                    shot.impact()
                    asteroid.split()

        

            



        #render
        screen.fill((0,0,0))
        for sprite in drawable:
            sprite.draw(screen)
            


        pygame.display.flip() 
        
        #clock
        delta_time = game_clock.tick(60) / 1000





if __name__ == "__main__":
    main()
