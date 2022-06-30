# Author: Hotaru
# SkyCastle - [FrameWork]

import pygame, random

# initializing
pygame.init()
score = 0

# window
screen = pygame.display.set_mode((1200, 900))

# background [800 x 600]
# background = pygame.image.load('background.png')

# window style
pygame.display.set_caption('-[Sky Castle]-')
icon = pygame.image.load('castle.png')
pygame.display.set_icon(icon)

# entity
class Entity:
    def __init__(self, icon, x, y, x_change=0, y_change=0):   
        self.img = pygame.image.load(icon)
        self.x = x
        self.y = y
        self.x_change = x_change
        self.y_change = y_change
    def run(self):
        self.x += self.x_change
        self.y += self.y_change
        # fixing boundaries
        if self.x > 1136:
            self.x = 1136
        elif self.x < 0:
            self.x = 0
        if self.y > 836:
            self.y = 836
        elif self.y < 0:
            self.y = 0
        screen.blit(self.img, (self.x, self.y))

# player
class Player(Entity):
    def __str__(self):
        return

# weed enemy
class Weed(Entity):
    def __init__(self, name='Weed'):
        super().__init__('enemy_weed.png', random.randint(50, 1136), random.randint(50, 400), 0.2)
        self.name = name
    def run(self):
        if self.x >= 1136:
            self.x_change *= -1
            self.y += 50
        elif self.x <= 0:
            self.x_change *= -1
            self.y += 50
        super().run()
    def reset(self):
        self.x = random.randint(50, 1136)
        self.y = random.randint(50, 400)

# projectile
class Bullet(Entity):
    count = 0
    def __init__(self, state='ready'):
        super().__init__('plunger.png', 0, 0, 0, 0.5)
        self.state = state
        Bullet.count = 1
    def fire(self):
        self.state = 'fired'
    def bullet(self):
        if self.state == 'fired':
            self.y -= self.y_change
        if self.y < -32:
            self.state = 'ready'
        screen.blit(self.img, (self.x, self.y))
    def reset(self):
        self.x = 0
        self.y = -32
    @staticmethod
    def isCollision(bullet, enemy):
        if bullet.x < enemy.x + 64 and bullet.x > enemy.x - 32:
            if bullet.y < enemy.y + 64 and bullet.y > enemy.y - 32:
                return True

# generating entities
player = Player('player.png', 568, 720)
enemy1 = Weed()
bullet = Bullet()

# game loop
running = True
while running:
    
    # RGB base color
    screen.fill((51, 153, 255))
    # screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # keyboard interaction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player.y_change += 0.3
            if event.key == pygame.K_w:
                player.y_change -= 0.3
            if event.key == pygame.K_d:
                player.x_change += 0.3
            if event.key == pygame.K_a:
                player.x_change -= 0.3
            
            if event.key == pygame.K_SPACE and bullet.state == 'ready':
                bullet.x = player.x + 16
                bullet.y = player.y
                bullet.fire()
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player.y_change -= 0.3
            if event.key == pygame.K_w:
                player.y_change += 0.3
            if event.key == pygame.K_d:
                player.x_change -= 0.3
            if event.key == pygame.K_a:
                player.x_change += 0.3
    
    player.run()
    enemy1.run()
    if bullet.state == 'fired':
        bullet.bullet()
    if bullet.isCollision(bullet, enemy1):
        bullet.reset()
        enemy1.reset()
        score += 1
        print(f'{enemy1.name} was yeeted: score +1\nCurrent score: {score}')
    pygame.display.update()




