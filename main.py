import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Inititialize font required to render text
    pygame.font.init()
    font = pygame.font.SysFont(None, 30) # Can change the size of the text

    i = 0
    while i < 5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen
        screen.fill((0, 0, 0))
        
        # Tick the clock and get the fps
        clock.tick(60)
        fps = clock.get_fps()
        
        # dt = clock.tick() / 1000
        # print(f"delta time: {dt}")

        # Render FPS text
        fps_text = font.render(f"FPS: {fps:.2f}", True, (255, 0, 0))
        screen.blit(fps_text, (10, 10))

        # Update display
        pygame.display.flip()
        print(f"FPS: {fps:.2f}")

if __name__ == "__main__":
    main()
