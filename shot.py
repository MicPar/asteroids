import pygame
from circleshape import *
from constants import *

# Base class for game objects
class Shot(CircleShape):
    def __init__(self, player):
        super().__init__(player.position.x, player.position.y, SHOT_RADIUS)
        self.velocity = (pygame.Vector2(0, 1).rotate(player.rotation) * SHOT_SPEED) + player.velocity

    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

    def update(self, delta_time):
        self.position += self.velocity * delta_time


    def collision_check(self, other_object):
        if pygame.Vector2.distance_to(self.position, other_object.position) < (self.radius + other_object.radius):
            print("Collision!")
            return True
        else:
            return False