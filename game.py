import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("i like cars")
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Game logic and drawing code can go here
            
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()