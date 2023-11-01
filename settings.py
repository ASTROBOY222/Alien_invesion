

class Settings():

    def __init__(self):
        # window settings
        self.screen_width = 900
        self.screen_height = 500
        self.bg_color = "#808080"
        # ship settings
        self.ship_speed_factor = 0.5
        self.ship_limit = 3
        # bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3
        self.bullet_miss = 3
        # Aliens settings
        self.alien_speed_factor = 0.1
        self.fleet_drop_speed = 5
        # direction; 1 represent right and -1 represent left
        self.fleet_direction = 1
