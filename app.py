import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Real-time Projectile Motion")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

g = 9.81    # m / s2
speed = 20  # m / s
angle = 90  # องศา


PPM = 20  # Pixels Per Meter 

start_x = 0
start_y = 0

x_m = 0
y_m = start_y / PPM 

theta = math.radians(angle)
vx = speed * math.cos(theta)
vy = speed * math.sin(theta)

trajectory = []
running = True
clock = pygame.time.Clock()

time = 0

while running:
    dt = clock.tick(60) / 1000.0 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if y_m >= 0:
        x_m = x_m + (vx * dt)
        y_m = y_m + (vy * dt)

        # v = a x t
        # dv = -g x t
        # v = v + dv
        # v = v + (-g x t)
        # v = v - g x t
        vy = vy - (g * dt)
    else:
        y_m = 0
        vx = 0
        vy = 0

    screen_x = start_x + (x_m * PPM)
    

    screen_y = HEIGHT - 10 - (y_m * PPM)

    if vx != 0: 
        trajectory.append((screen_x, screen_y))
        time += dt

    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, (0, HEIGHT-10), (WIDTH, HEIGHT-10), 2)

    if len(trajectory) > 1:
        pygame.draw.lines(screen, BLUE, False, trajectory, 2)

    pygame.draw.circle(screen, RED, (int(screen_x), int(screen_y)), 10)
    
    font = pygame.font.SysFont(None, 24)
    img = font.render(f"Time: {time:.4f}s", True, BLACK)
    screen.blit(img, (10, 10))
    img = font.render(f"Height: {y_m:.2f}m", True, BLACK)
    screen.blit(img, (10, 30))
    img = font.render(f"Distance: {x_m:.2f}m", True, BLACK)
    screen.blit(img, (10, 50))
    img = font.render(f"Y Velocity: {vy:.2f}m/s", True, BLACK)
    screen.blit(img, (10, 70))

    pygame.display.flip()
    

pygame.quit()