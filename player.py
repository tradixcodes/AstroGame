import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__ (self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

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

    def shoot(self):
        if self.timer > 0:
            return

        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = direction * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        if self.timer > 0:
            self.timer -= dt
            if self.timer < 0:
                self.timer = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(1, dt)
        if keys[pygame.K_d]:
            self.rotate(-1, dt)
        if keys[pygame.K_w]:
            self.move(1, dt)
        if keys[pygame.K_s]:
            self.move(-1, dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
