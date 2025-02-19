
import pygame
from constants import *
from circleshape import *
from shot import *
from debris import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, (255, 255, 255),self.triangle(), 2)

    def rotate(self, delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time

    def move(self, delta_time):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * PLAYER_SPEED * delta_time

    def shoot(self):
        if self.timer > 0:
            pass
        else:
            self.timer = PLAYER_SHOOT_COOLDOWN
            Shot(self)

    def impact(self):
        for i in range(50):
            debris = Debris(self, 200)
        self.kill()




    def update(self, delta_time):
        if self.timer > 0:
            self.timer -= delta_time

        self.position += self.velocity * delta_time

        self.edge_wrap(self.radius)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-delta_time)
        if keys[pygame.K_d]:
            self.rotate(delta_time)

        if keys[pygame.K_w]:
            self.move(delta_time)
        if keys[pygame.K_s]:
            self.move(-delta_time)

        if keys[pygame.K_SPACE]:
            self.shoot()