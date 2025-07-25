import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

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

    # Player Object groups
    update_group = pygame.sprite.Group()
    draw_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    Player.containers = (update_group, draw_group)
    Asteroid.containers = (asteroid_group, update_group, draw_group)
    AsteroidField.containers = (update_group,)

    # Player object instantiation
    Tradix = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Astroworld = AsteroidField()

    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return running == False

        # Fill the screen
        screen.fill((0, 0, 0))
        
        # Tick the clock and get the fps
        clock.tick(60)
        fps = clock.get_fps()

        dt = clock.tick(60) / 1000 #delta time(dt) is the time between two frames; here in milliseconds for a clock tick of 60 frames per second
        print(f"delta time: {dt}")
        
        # Render FPS text
        fps_text = font.render(f"FPS: {fps:.2f}", True, (255, 0, 0))
        screen.blit(fps_text, (10, 10))
        
        # allows me to rotate the player
        update_group.update(dt)

        # Re-render player on the screen
        for player in draw_group:
            player.draw(screen)

        # Update display
        pygame.display.flip()
        print(f"FPS: {fps:.2f}")

if __name__ == "__main__":
    main()
