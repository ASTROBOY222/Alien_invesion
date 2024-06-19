import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():

    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("alien invasion ")

    # make the play button.
    play_button = Button(ai_setting, screen, "Play")

    stats = GameStats(ai_setting)
    ship = Ship(ai_setting, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_setting, screen, ship, aliens)

    while True:
        gf.check_events(ai_setting, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_setting, stats, screen, ship, aliens, bullets)
            gf.update_aliens(ai_setting, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_setting, screen, stats, ship, aliens, bullets, play_button)

run_game()