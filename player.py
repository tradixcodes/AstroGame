import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__ (self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 1)

    def rotate(self, direction, dt):
        self.rotation += direction * PLAYER_TURN_SPEED * dt

    def move(self, direction, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += direction * forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(1, dt)
        if keys[pygame.K_d]:
            self.rotate(-1, dt)
        if keys[pygame.K_w]:
            self.move(1, dt)
        if keys[pygame.K_s]:
            self.move(-1, dt)
