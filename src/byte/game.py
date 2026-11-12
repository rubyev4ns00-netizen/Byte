import pygame
from pathlib import Path

from pygame import sprite

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
        #self.renderer = Renderer()
        print("Game initialized with screen_size:", self.screen_size, "repeat:", self.repeat, "radius:", self.radius)
        self.initialise()

    def initialise(self):
        pygame.init()
        pygame.display.init()
        self.run()

    def tick(self, clock, screen):
        self.handle_input()
        self.render(screen)
        clock.tick(self.framerate)

    def run(self):
        screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Byte")
        repeat_pause, repeat_delay = self.repeat
        pygame.key.set_repeat(repeat_pause, repeat_delay)
        self.running = True
        sprite = pygame.image.load(ASSETS_DIR / "ladybug.png").convert_alpha()
        sprite = pygame.transform.scale(sprite, (32, 32))
        clock = pygame.time.Clock()
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
        
    def handle_input(self):  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                #   self.running = False
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            #print(f"key pressed: left, radius = {self.radius}")
            self.radius = max(0, self.radius-1)
            self.x -= 5
        if keys[pygame.K_RIGHT]:
            #print(f"key pressed: right, radius = {self.radius}")
            self.radius = min(100, self.radius+1)
            self.x += 5
        if keys[pygame.K_UP]:
            #print(f"key pressed: up")
            self.y -= 5
        if keys[pygame.K_DOWN]:
            #print(f"key pressed: down")
            self.y += 5

        mouse1, mouse2, mouse3 = pygame.mouse.get_pressed(3)
        #print(f"mouse {mouse1}")
        x, y = pygame.mouse.get_pos()
        #print(f"position {x, y}")
        #pygame.draw.circle(screen, (y%100, x%50, 100), (x, y), self.radius)
