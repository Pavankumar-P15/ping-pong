import pygame
from game.game_engine import GameEngine

# Initialize pygame and mixer
pygame.init()
pygame.mixer.init()

# Load sound effects
paddle_hit_sound = pygame.mixer.Sound('sounds/paddle_hit.mp3')
wall_bounce_sound = pygame.mixer.Sound('sounds/wall_bounce.wav')
score_sound = pygame.mixer.Sound('sounds/score.wav')

# Screen setup
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong - Pygame Version")

# Colors
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game engine with sounds
engine = GameEngine(WIDTH, HEIGHT, paddle_hit_sound, wall_bounce_sound, score_sound)

def main():
    running = True
    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not engine.handle_input():
            break

        engine.update()
        engine.render(SCREEN)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()