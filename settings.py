class Settings:
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """Инициализирует настройки игры"""

        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        # Назначение цвета фона (RGB)
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed_factor = 1.5  # Скорость перемещения

        # Настройки пришельцев
        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

        # Параметры пули
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3
