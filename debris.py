import pygame
import random
from circleshape import *

# Base class for game objects
class Debris(CircleShape):
    def __init__(self, parent, force):
        super().__init__(parent.position.x, parent.position.y, random.uniform(1, max(3, parent.radius * 0.1)))
        self.velocity = parent.velocity + pygame.Vector2(random.uniform(-force, force), random.uniform(-force, force))
        self.despawn_timer = 5
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

    def update(self, delta_time):
        self.despawn_timer -= delta_time
        if self.despawn_timer < 0:
            self.kill()
        self.position += self.velocity * delta_time


    def collision_check(self, other_object):
        if pygame.Vector2.distance_to(self.position, other_object.position) < (self.radius + other_object.radius):
            return True
        else:
            return False