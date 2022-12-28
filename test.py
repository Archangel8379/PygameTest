import pygame
from sys import exit

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test")

def draw_window():
 WIN.fill((255,255,255))
 pygame.display.update()


FPS = 60

def main():

    clock = pygame.time.Clock()

    while True:

        try:

            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

        except KeyboardInterrupt:
            exit()
                
if __name__ == "__main__":
    main()
