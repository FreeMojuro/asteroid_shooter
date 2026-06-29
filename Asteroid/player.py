from circleshape import *
from constants import *
from pygame import *
from shot import *

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
        self.velocity = pygame.Vector2(0, 0)
        self.lives = 3
        self.invincibility_timer = 0.0
    
    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    def draw(self,screen):
        if self.invincibility_timer > 0:
            if int(self.invincibility_timer * 10) % 2 == 0:
                return  # skip drawing every other frame to create a flash
            
            
        
        
        
        
        pygame.draw.polygon(screen,"white",self.triangle(),LINE_WIDTH)
        
        
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        return self.rotation
        
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            if self.shot_cooldown <= 0:
                
                self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
                self.shoot()
            
            
            
            
            
        self.shot_cooldown -= dt
        self.velocity *= PLAYER_DRAG
        self.position += self.velocity
        if self.invincibility_timer > 0:
            self.invincibility_timer -= dt
        super().update(dt)
        
    
    
    def move(self,dt):   
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * PLAYER_ACCELERATION * dt
        
        
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        direction_vector = pygame.Vector2(0,1)
        shot.velocity = direction_vector.rotate(self.rotation) * PLAYER_SHOOT_SPEED
    
    def hit(self):
        self.lives -=1
        if self.lives <= 0:
            return True 
        else:
            self.respawn()
            return False
            
    def respawn(self):
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.velocity = pygame.Vector2(0, 0)
        self.invincibility_timer = 3.0
    
    def is_invincible(self):
        return self.invincibility_timer > 0 
            
    