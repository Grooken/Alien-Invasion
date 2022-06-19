import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """Инициализирует pygame, settings и объекты экрана"""

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание корабля
    ship = Ship(ai_settings, screen)
    # Создание группы для хранения пуль и пришельцев.
    bullets = Group()
    aliens = Group()
    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, aliens)

    # Запуск основного цикла игры.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)


run_game()
