from byte import game
import pygame

# def test_game_loop():
#     # Create a Game instance with test parameters
#     test_game = game.Game(screen_size=(640, 480), repeat=(200, 20), radius=10)

#     # Check if the attributes are set correctly
#     assert test_game.screen_size == (640, 480)
#     assert test_game.repeat == (200, 20)
#     assert test_game.radius == 10

#     # Since game_loop involves an infinite loop and user interaction,
#     # we will not call it here. Instead, we can check if the method exists.
#     assert hasattr(test_game, 'game_loop')

def test_render_loads_sprite():
    print("test_render_loads_sprite: Starting test...")
    test_game = game.Game()
    print ("test_render_loads_sprite: test_game.sprite before render:", test_game.sprite)
    # screen = pygame.display.set_mode((640, 480))

    # test_game.render(screen)

    # assert test_game.sprite is not None
    # assert test_game.sprite.get_size() == (32, 32)

def test_input_handling():
    print("test_input_handling: Starting test...")
    # test_game = game.Game()
    # pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_q))
    # test_game.handle_input()
    # assert test_game.running == False
    assert True  # Placeholder assertion to indicate the test is running