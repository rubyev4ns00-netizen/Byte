import pygame
import os
import sys

def game_loop():

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.key.set_repeat(300, 30)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                print(f"key pressed: left")
            if keys[pygame.K_RIGHT]:
                print(f"key pressed: right")
            if keys[pygame.K_UP]:
                print(f"key pressed: up")
            if keys[pygame.K_DOWN]:
                print(f"key pressed: down")
            mouse1, mouse2, mouse3 = pygame.mouse.get_pressed(3)
            print(f"mouse {mouse1}")
            x, y = pygame.mouse.get_pos()
            print(f"position {x, y}")
            pygame.draw.circle(screen, (x%255, y%255, 0), (x, y), 100)

        pygame.display.flip()
        clock.tick(60)


game_loop()