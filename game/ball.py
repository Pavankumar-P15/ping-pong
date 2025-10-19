import pygame
import random

class Ball:
    def __init__(self, x, y, dx, dy, width, height,
                 paddle_hit_sound, wall_bounce_sound, score_sound):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.width = width
        self.height = height
        self.size = 15

        self.paddle_hit_sound = paddle_hit_sound
        self.wall_bounce_sound = wall_bounce_sound
        self.score_sound = score_sound

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off top/bottom
        if self.y <= 0 or self.y >= self.height - self.size:
            self.dy = -self.dy
            self.wall_bounce_sound.play()

    def check_collision(self, player, ai):
        ball_rect = self.rect()
        if ball_rect.colliderect(player.rect()):
            self.dx = abs(self.dx)
            self.paddle_hit_sound.play()
        elif ball_rect.colliderect(ai.rect()):
            self.dx = -abs(self.dx)
            self.paddle_hit_sound.play()

    def reset(self):
        self.x = self.width // 2
        self.y = self.height // 2
        self.dx = random.choice([-7, 7])
        self.dy = random.choice([-7, 7])

    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)