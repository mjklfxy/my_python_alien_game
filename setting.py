class Settings:
    """存储外星人游戏中所有设置的类"""

    def __init__(self):
        self.screen_width = 900
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.ship_speed = 5

        # 子弹设置
        self.bullet_speed = 5
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bulley_allowed = 300

        self.alien_speed = 10
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.ship_left=3
