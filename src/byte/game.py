import pygame

class Game:
    def __init__(
        self,
        screen_size=(800,600),
        repeat=(300,30),
        radius=5):

        self.screen_size=screen_size
        self.repeat=repeat
        self.radius=radius

    def game_loop(self):
        pygame.init()
        screen = pygame.display.set_mode(self.screen_size)
        repeat_pause, repeat_delay = self.repeat
        pygame.key.set_repeat(repeat_pause, repeat_delay)

        clock = pygame.time.Clock()
        running = True
        radius = 5

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    print(f"key pressed: left, radius = {self.radius}")
                    self.radius = max(0, self.radius-1)
                if keys[pygame.K_RIGHT]:
                    print(f"key pressed: right, radius = {self.radius}")
                    self.radius = min(100, self.radius+1)
                if keys[pygame.K_UP]:
                    print(f"key pressed: up")
                if keys[pygame.K_DOWN]:
                    print(f"key pressed: down")
                mouse1, mouse2, mouse3 = pygame.mouse.get_pressed(3)
                print(f"mouse {mouse1}")
                x, y = pygame.mouse.get_pos()
                print(f"position {x, y}")
                pygame.draw.circle(screen, (x%255, y%255, 0), (x, y), self.radius)

            pygame.display.flip()
            clock.tick(60)

def main():
    byte_game = Game()
    byte_game.game_loop()

if __name__ == '__main__':
    main()