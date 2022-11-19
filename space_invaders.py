import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load Images
RED_SPACESHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACESHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACESHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Player Ship
YELLOW_SPACESHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Load Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Load Background Image
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y, 50, 50))
        #window.blit(self.ship_img, (self.x, self.y))
        #for laser in self.lasers:
            #laser.draw(window)
       
def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    player_velocity = 5

    ship = Ship(300, 650)
    
    #player = Player(300, 630)

    clock = pygame.time.Clock()
    
    def redraw_window():
        WIN.blit(BG, (0,0))
        # Draw Text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        ship.draw(WIN)
        
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_velocity > 0: # Left
             ship.x -= player_velocity
        if keys[pygame.K_d] and player.x + player_velocity + player.get_width() < WIDTH: # Right
             ship.x += player_velocity
        if keys[pygame.K_w] and player.y - player_velocity > 0: # Up
             ship.y -= player_velocity
        if keys[pygame.K_s] and player.y + player_velocity + player.get_height() + 15 < HEIGHT: # Down
             ship.y += player_velocity
        if keys[pygame.K_SPACE]:
            player.shoot()

main()
