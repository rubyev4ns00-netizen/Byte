import os
os.environ["SDL_VIDEODRIVER"] = "dummy"  # no real window needed

import pygame
import pytest

@pytest.fixture(autouse=True, scope="session")
def pygame_display():
    pygame.display.init()
    pygame.display.set_mode((1, 1))
    yield
    pygame.quit()