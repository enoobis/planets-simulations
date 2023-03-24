import pygame, sys
from pygame.locals import QUIT
import random

# initialize pygame
pygame.init()

# set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Planets Simulation")

# set up the clock
clock = pygame.time.Clock()

# define some colors
black = (0, 0, 0)
white = (255, 255, 255)

# define the planet class
class Planet(pygame.sprite.Sprite):
    def __init__(self, x, y, size, color):
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mass = size
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)
        
    def apply_force(self, force):
        acceleration = force / self.mass
        self.acceleration += acceleration
        
    def update(self):
        self.velocity += self.acceleration
        self.rect.move_ip(self.velocity.x, self.velocity.y)
        self.acceleration *= 0
        if self.rect.left > screen_width:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = screen_width
        if self.rect.top > screen_height:
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = screen_height
            
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
# create some planets
planets = pygame.sprite.Group()
for i in range(10):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    size = random.randint(10, 50)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    planet = Planet(x, y, size, color)
    planets.add(planet)

# main game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # clear the screen
    screen.fill(black)
    
    # update the planets
    for planet in planets:
        planets.remove(planet)
        for other_planet in planets:
            if planet != other_planet:
                dx = other_planet.rect.centerx - planet.rect.centerx
                dy = other_planet.rect.centery - planet.rect.centery
                distance = pygame.math.Vector2(dx, dy).length()
                direction = pygame.math.Vector2(dx, dy).normalize()
                force = direction * (planet.mass * other_planet.mass) / (distance ** 2)
                planet.apply_force(force)
        planet.update()
        planets.add(planet)
        planet.draw(screen)
    
    # update the display
    pygame.display.flip()
    
    # cap the framerate
    clock.tick(60)

# quit pygame
pygame.quit()