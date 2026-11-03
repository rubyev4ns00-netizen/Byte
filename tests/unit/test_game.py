from byte import game
import pygame

def test_game_loop():
    # Create a Game instance with test parameters
    test_game = game.Game(screen_size=(640, 480), repeat=(200, 20), radius=10)

    # Check if the attributes are set correctly
    assert test_game.screen_size == (640, 480)
    assert test_game.repeat == (200, 20)
    assert test_game.radius == 10

    # Since game_loop involves an infinite loop and user interaction,
    # we will not call it here. Instead, we can check if the method exists.
    assert hasattr(test_game, 'game_loop')

def test_get_image():
    # Create a Game instance
    test_game = game.Game()

    # Create a dummy sprite surface for testing
    dummy_sprite = pygame.Surface((32, 32)).convert_alpha()

    # Call the get_image method
    image = test_game.get_image(dummy_sprite, 16, 16)

    # Check if the returned image has the correct size
    assert image.get_size() == (16, 16)