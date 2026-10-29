import pygame
from pygame import sprite

class Game:
    def __init__(
        self,
        screen_size=(800,600),
        repeat=(300,30),
        radius=5):

        self.screen_size=screen_size
        self.repeat=repeat
        self.radius=radius

        pygame.display.init()


    def game_loop(self):
        pygame.init()
        screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Byte")
        repeat_pause, repeat_delay = self.repeat
        pygame.key.set_repeat(repeat_pause, repeat_delay)

        clock = pygame.time.Clock()
        running = True
        radius = 5
        a = 0
        b = 0

        background_color = (0, 255, 0) # green
        sprite = pygame.image.load("ladybug.png").convert_alpha()


        while running:
            screen.fill(background_color)
            screen.blit(sprite, (a, b))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    print(f"key pressed: left, radius = {self.radius}")
                    self.radius = max(0, self.radius-1)
                    a = a-5
                if keys[pygame.K_RIGHT]:
                    print(f"key pressed: right, radius = {self.radius}")
                    self.radius = min(100, self.radius+1)
                    a = a+5
                if keys[pygame.K_UP]:
                    print(f"key pressed: up")
                    b = b-5
                if keys[pygame.K_DOWN]:
                    print(f"key pressed: down")
                    b = b+5

                
                mouse1, mouse2, mouse3 = pygame.mouse.get_pressed(3)
                print(f"mouse {mouse1}")
                x, y = pygame.mouse.get_pos()
                print(f"position {x, y}")
                #pygame.draw.circle(screen, (y%100, x%50, 100), (x, y), self.radius)
                

            pygame.display.flip()
            clock.tick(60)
    def get_image(sheet, width, height):
        image = pygame.Surface((width, height)).convert_alpha()

        return image
        frame_0 = get_image(sprite, 16, 16)



def main():
    byte_game = Game()
    byte_game.game_loop()
    byte_game.get_image(sprite, 16, 16)


if __name__ == '__main__':
    main()