class Settings:
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """Инициализирует статические настройки игры"""

        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        # Назначение цвета фона (RGB)
        self.bg_color = (132, 162, 164)

        # Настройки корабля
        self.ship_limit = 3
        # Настройки пришельцев
        self.fleet_drop_speed = 15
        # Параметры пули
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""

        # Скорость корабля, пули, пришельцев
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.1
        # fleet_direction = 1 обозначает движение флота вправо; а -1 - влево.
        self.fleet_direction = 1
        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и "стоимость" пришельцев."""

        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
