import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planets Simulation Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Define constants
G = 1
DT = 0.1

# Define classes
class Planet:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self):
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), int(self.mass))

    def update(self, planets):
        self.ax = 0
        self.ay = 0
        for planet in planets:
            if planet != self:
                dx = planet.x - self.x
                dy = planet.y - self.y
                d = math.sqrt(dx**2 + dy**2)
                f = G * self.mass * planet.mass / (d**2)
                theta = math.atan2(dy, dx)
                fx = f * math.cos(theta)
                fy = f * math.sin(theta)
                self.ax += fx / self.mass
                self.ay += fy / self.mass
        self.vx += self.ax * DT
        self.vy += self.ay * DT
        self.x += self.vx * DT
        self.y += self.vy * DT

# Create stars
stars = []
num_stars = random.randint(1, 5)
for i in range(num_stars):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    stars.append((x, y))

# Create planets
planets = []
num_planets = random.randint(5, 10)
for i in range(num_planets):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    mass = random.randint(10, 50)
    planet = Planet(x, y, mass)
    planets.append(planet)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update planets
    for planet in planets:
        planet.update(planets)

    # Draw stars
    for star in stars:
        pygame.draw.circle(window, WHITE, star, 2)

    # Draw planets
    for planet in planets:
        planet.draw()

    # Update display
    pygame.display.update()

    # Clear window
    window.fill(BLACK)

# Quit Pygame
pygame.quit()