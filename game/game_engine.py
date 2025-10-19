import pygame
from .paddle import Paddle
from .ball import Ball

WHITE = (255, 255, 255)

class GameEngine:
    def __init__(self, width, height, paddle_hit_sound, wall_bounce_sound, score_sound):
        self.width = width
        self.height = height

        self.paddle_hit_sound = paddle_hit_sound
        self.wall_bounce_sound = wall_bounce_sound
        self.score_sound = score_sound

        self.paddle_width = 10
        self.paddle_height = 100

        self.player = Paddle(10, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ai = Paddle(width - 20, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ball = Ball(width // 2, height // 2, 7, 7, width, height,
                         paddle_hit_sound, wall_bounce_sound, score_sound)

        self.player_score = 0
        self.ai_score = 0
        self.winning_score = 5
        self.game_over = False
        self.winner_text = ""

        # Fonts
        self.font = pygame.font.SysFont("Arial", 30)
        self.large_font = pygame.font.SysFont("Arial", 60)
        self.small_font = pygame.font.SysFont("Arial", 24)

    def reset_game(self, winning_score):
        self.winning_score = winning_score
        self.player_score = 0
        self.ai_score = 0
        self.game_over = False
        self.winner_text = ""
        self.ball.reset()

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if self.game_over:
            if keys[pygame.K_3]:
                self.reset_game(3)
            elif keys[pygame.K_5]:
                self.reset_game(5)
            elif keys[pygame.K_7]:
                self.reset_game(7)
            elif keys[pygame.K_ESCAPE]:
                return False
        else:
            if keys[pygame.K_w]:
                self.player.move(-10, self.height)
            if keys[pygame.K_s]:
                self.player.move(10, self.height)

        return True

    def update(self):
        if self.game_over:
            return

        self.ball.move()
        self.ball.check_collision(self.player, self.ai)

        if self.ball.x <= 0:
            self.ai_score += 1
            self.score_sound.play()
            self.ball.reset()
        elif self.ball.x >= self.width:
            self.player_score += 1
            self.score_sound.play()
            self.ball.reset()

        self.ai.auto_track(self.ball, self.height)

        if self.player_score >= self.winning_score:
            self.winner_text = "Player Wins!"
            self.game_over = True
        elif self.ai_score >= self.winning_score:
            self.winner_text = "AI Wins!"
            self.game_over = True

    def render(self, screen):
        if self.game_over:
            winner_surface = self.large_font.render(self.winner_text, True, WHITE)
            winner_rect = winner_surface.get_rect(center=(self.width / 2, self.height / 2 - 50))
            screen.blit(winner_surface, winner_rect)

            instructions = [
                "Play Again:",
                "Best of 3 (Press 3)",
                "Best of 5 (Press 5)",
                "Best of 7 (Press 7)",
                "Exit (Press ESC)"
            ]
            y_offset = self.height / 2 + 20
            for line in instructions:
                line_surface = self.small_font.render(line, True, WHITE)
                line_rect = line_surface.get_rect(center=(self.width / 2, y_offset))
                screen.blit(line_surface, line_rect)
                y_offset += 30
        else:
            pygame.draw.rect(screen, WHITE, self.player.rect())
            pygame.draw.rect(screen, WHITE, self.ai.rect())
            pygame.draw.ellipse(screen, WHITE, self.ball.rect())
            pygame.draw.aaline(screen, WHITE, (self.width//2, 0), (self.width//2, self.height))

            player_text = self.font.render(str(self.player_score), True, WHITE)
            ai_text = self.font.render(str(self.ai_score), True, WHITE)
            screen.blit(player_text, (self.width//4, 20))
            screen.blit(ai_text, (self.width * 3//4, 20))