import pygame
import random
import math

# Initialize pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planets Simulation")

# Define colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Define gravitational constant
G = 0.1

# Define planet class
class Planet:
    def __init__(self, x, y, radius, mass, vx, vy):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.vx = vx
        self.vy = vy

    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, (int(self.x), int(self.y)), self.radius)

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def apply_gravity(self, planet):
        dx = planet.x - self.x
        dy = planet.y - self.y
        dist = math.sqrt(dx**2 + dy**2)
        if dist == 0:
            return
        force = G * self.mass * planet.mass / (dist**2)
        angle = math.atan2(dy, dx)
        fx = math.cos(angle) * force
        fy = math.sin(angle) * force
        self.vx += fx / self.mass
        self.vy += fy / self.mass

# Generate random number of planets and stars
num_planets = random.randint(2, 5)
num_stars = random.randint(1, 2)

# Generate planets and stars
planets = []
for i in range(num_planets):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    radius = random.randint(5, 20)
    mass = radius * 10
    vx = random.randint(-1, 1)
    vy = random.randint(-1, 1)
    planet = Planet(x, y, radius, mass, vx, vy)
    planets.append(planet)

# Start the simulation loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the planets and stars
    for planet in planets:
        planet.draw(screen)
    for i in range(num_stars):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        radius = random.randint(1, 3)
        pygame.draw.circle(screen, RED, (x, y), radius)

    # Apply gravity to each planet
    for i, planet in enumerate(planets):
        for planet2 in planets[i+1:]:
            planet.apply_gravity(planet2)
            planet2.apply_gravity(planet)

    # Move the planets
    for planet in planets:
        planet.move()

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()