import pygame
import birdscript
pygame.init()
bg = pygame.image.load('flappybird/flappyimages/background.png')
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('flappy bird')

bird = birdscript.Bird(200, 200, 64, 64)
jumpCount = 10
isJump = False

def redrawGameWindow():
    win.blit(bg,(0, 0))
    pygame.display.update()

run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    bird.move()
    

    redrawGameWindow()


    
    

