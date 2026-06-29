from constants import *
from pygame import *
import pygame
from logger import *
from circleshape import *
from player import *
from asteroidfield import *
import sys
from sys import *
import random
from particle import *




def main() -> None:
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    score = 0
    
    stars = []
    for _ in range(100):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        stars.append((x, y))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)
    Particle.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    font = pygame.font.Font(None, 36)
    
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for star in stars:
            pygame.draw.circle(screen, "white", star, 1)
        dt = clock.tick(60) / 1000
        for x in drawable:
            x.draw(screen)
        for y in updatable:
            y.update(dt)
        
        if not player.is_invincible():
            for asteroid in asteroids:
                if asteroid.collides_with(player) is True:
                    log_event("player_hit")
                    result = player.hit()
                    if result is True:
                        print("Game over!")
                        sys.exit()
                    break
            
        for shot in shots:
            for asteroid in asteroids:
                if asteroid.collides_with(shot) is True:
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    score += 50
                    # Spawn particles at the asteroid's position
                    for i in range(10):
                        Particle(asteroid.position.x, asteroid.position.y)
                    break
                    
                    
                
            
        text_surface = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))      # top-left corner    
        lives_surface = font.render(f"Lives: {player.lives}", True, (255, 255, 255))
        screen.blit(lives_surface, (10, 40))  # just below the score
        
        display.flip()
        


if __name__ == "__main__":
    main()