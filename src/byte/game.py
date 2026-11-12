import pygame
from pygame import sprite
from byte.inputhandler import InputHandler
from pathlib import Path

ASSETS_DIR = Path(__file__).parent  # src/byte/

class Game:
    def __init__(
        self,
        screen_size=(800,600),
        repeat=(300,30),
        radius=5):

        # These are the member variables 
        self.screen_size=screen_size
        self.repeat=repeat
        self.radius=radius
        self.running = True
        self.x = 0
        self.y = 0
        self.framerate = 60
        self.sprite = None
        #self.state = State()
        #self.levels = Level[]
        self.inputhandler = InputHandler()
        #self.renderer = Renderer()
        print("Game initialized with screen_size:", self.screen_size, "repeat:", self.repeat, "radius:", self.radius)
        self.initialise()

    def initialise(self):
        pygame.init()
        pygame.display.init()
        screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Byte")
        repeat_pause, repeat_delay = self.repeat
        pygame.key.set_repeat(repeat_pause, repeat_delay)
        sprite = pygame.image.load(ASSETS_DIR / "ladybug.png").convert_alpha()
        sprite = pygame.transform.scale(sprite, (32, 32))
        clock = pygame.time.Clock()
        self.run(clock, screen)

    def tick(self, clock, screen):
        x, y, event = self.inputhandler.handle_input(pygame, self.x, self.y)
        if event == pygame.QUIT:
            self.running = False
        else:
            self.x = x
            self.y = y
        self.render(screen)
        clock.tick(self.framerate)

    def run(self, clock, screen):
        self.running = True
        while self.running:
            self.tick(clock, screen)

        self.exit()

    def exit(self):
        pygame.quit()
        return

    def render(self, screen):
        if self.sprite is None:
            sprite = pygame.image.load(ASSETS_DIR / "ladybug.png").convert_alpha()
            self.sprite = pygame.transform.scale(sprite, (32, 32))
      
        screen.fill((0, 255, 0)) #green
        screen.blit(self.sprite, (self.x, self.y))
        pygame.display.flip()
