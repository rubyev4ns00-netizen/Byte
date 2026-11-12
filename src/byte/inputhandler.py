class InputHandler:
    def __init__(self):
        # self.keys_pressed = set()

    # def update(self):
    #     self.keys_pressed.clear()

    # def is_key_pressed(self, key):
    #     return key in self.keys_pressed
        return

    def handle_input(self, pygame, x, y):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return (None, None, pygame.QUIT)
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                #   self.running = False
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            return (x-5, y, pygame.K_LEFT)

        if keys[pygame.K_RIGHT]:
            return (x+5, y, pygame.K_RIGHT)

        if keys[pygame.K_UP]:
            return (x, y-5, pygame.K_UP)
        
        if keys[pygame.K_DOWN]:
            return (x, y+5, pygame.K_DOWN)

        mouse1, mouse2, mouse3 = pygame.mouse.get_pressed(3)
        x, y = pygame.mouse.get_pos()
        return (x, y, pygame.MOUSEBUTTONDOWN)
        #print(f"position {x, y}")
        #pygame.draw.circle(screen, (y%100, x%50, 100), (x, y), self.radius)