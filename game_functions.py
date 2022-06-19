import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Реагирует на нажатие клавиш."""

    # Перемещать корабль в (право\лево) при нажатии клавиш
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """Реагирует на отпускание клавиш."""

    # Завершение перемещения корабля в
    # (право\лево) после отжатия клавиш
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Обрабатывает нажатия клавиш и события мыши"""

    for event in pygame.event.get():
        # Закрытие программы (отслеживает нажатие на крестик)
        if event.type == pygame.QUIT:
            sys.exit()
        # Действия при нажатии клавиши
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        # Действия при отжатии клавиши
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets, alien):
    """Обновляет изображения на экране и отображает
    новый экран с учетом новых позиций игровых элементов"""

    # При каждом проходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    # Все пули выводятся позади изображений корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Выводим корабль на экран
    ship.blitme()
    # Выводим пришельца на экран
    alien.blitme()
    # Отображение последнего прорисованного экрана
    pygame.display.flip()


def update_bullets(bullets):
    """Обновляет позиции пуль и уничтожает старые пули
    которые вышли за предел экрана."""

    # Обновление позиций пуль.
    bullets.update()
    # Удаление пуль, вышедших за край экрана.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Выпускает пулю, если максимум еще не достигнут."""
    # Создание новой пули и включение ее в группу bullets
    # После проверки количества активных пуль "bullets_allowed"
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
