from circleshape import *
import circleshape
from pygame import *
from constants import *
import random





class Particle(CircleShape):
    def __init__(self, x, y):
        self.radius = random.uniform(2, 5)
        super().__init__(x,y,self.radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(
            random.uniform(-150, 150),
            random.uniform(-150, 150)
        )
        self.lifetime = random.uniform(0.3, 0.6)  # seconds
        
        
        
        
        
    def update(self, dt):
        self.position += self.velocity * dt
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 140, 0), (int(self.position.x), int(self.position.y)), int(self.radius))
    