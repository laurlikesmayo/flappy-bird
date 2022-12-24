import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
birdy = pygame.image.load('flappybird/flappyimages/birdSprite.png')

class Bird():
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.isJump = False
        self.jumpCount = 10
        self.vel = 0
        self.tick_count = 0

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y
    
    def move(self):
        self.tick_count += 1

        d = self.vel * self.tick_count + 1.5*self.tick_count**2
        if d >=16:
            d = 16

        if d <0:
            d-=2

        self.y = self.y + d
        win.blit(birdy, (self.x, self.y))
        