import pygame
import time 

x = 800
y = 600

pygame.init()
vid = pygame.display.set_mode((x,y))
pygame.display.set_caption('простая игра')

men_u = pygame.image.load('C:/my_casino/game_on_python/print1.png').convert()
men_u  = pygame.transform.scale(men_u , (200 , 200))

men_t = pygame.image.load('C:/my_casino/game_on_python/print2.png').convert()
men_t  = pygame.transform.scale(men_t , (200 , 200))

game_over = False


men_x = x / 2
men_y = y / 2

speed = 5

speed_for_jump = 7

men = men_u

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True


            if event.key == pygame.K_a:
                men = men_t
                men_x -= speed


            if event.key == pygame.K_d:
                men = men_u
                men_x +=speed


            if event.key == pygame.K_SPACE:
                men_y -= speed_for_jump



    vid.fill((0,0,0))
    vid.blit(men , (men_x, men_y))
    pygame.display.flip()
