import pygame

class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 7

    def move(self, dy, screen_height):
        self.y += dy
        self.y = max(0, min(self.y, screen_height - self.height))

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def auto_track(self, ball, screen_height):
        """AI tracks the ball but with a speed limit and reaction delay."""
        target_y = ball.y - self.height / 2
    
    # Add a small reaction delay (AI won't move every frame)
        import random
        if random.random() < 0.85:  # 85% chance to react each frame
            if self.y < target_y:
                self.y += min(self.speed, target_y - self.y)
            elif self.y > target_y:
                self.y -= min(self.speed, self.y - target_y)
    
    # Ensure paddle stays within screen
        self.y = max(0, min(self.y, screen_height - self.height))
