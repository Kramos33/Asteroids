import pygame
import random
from circleshape import CircleShape
from constants import *




class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        if new_radius < ASTEROID_MIN_RADIUS:
            return []
        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2 * 1.2
        return [asteroid1, asteroid2]



