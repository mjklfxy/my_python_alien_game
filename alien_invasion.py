import random
import sys
from time import sleep

import pygame
from ship import Ship
from setting import Settings
from bullet import Bullet
from Alien import Alien
from  game_stats import GameStats

class AlienInvasion:
    """管理游戏资源和行为"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # 创建存储游戏统计信息的
        self.stats = GameStats(self)

        self.clock = pygame.time.Clock()

        # 实例化船
        self.ship = Ship(self)
        # self.bg_color = (230,230,230)
        self.bullets = pygame.sprite.Group()
        # 实例化外星人
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)
            # print(len(self.bullets))

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            # print( event)
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)

    def _update_bullets(self):
        """更新子弹的位置，并删除已消失的子弹"""
        self.bullets.update()
        # 删除屏幕外的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        collisions=pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            self._create_fleet()

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        # rect=pygame.image.load('images/bg.bmp').get_rect()
        # rect.midbottom = self.screen.get_rect().midbottom
        # self.screen.blit(pygame.image.load('images/bg.bmp'), rect)
        self.ship.blitme()
        self.ship.update()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _check_keydown(self, event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # 上下移动
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def _check_keyup(self, event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def fire_bullet(self, fire_bullet=True):
        """创建一颗子弹，并将其加入到编组bullets中"""
        if (len(self.bullets) < self.settings.bulley_allowed):
            self.bullets.add(Bullet(self))

        # pass

    def _create_fleet(self):
        """创建一个外星舰队"""
        # 创建一个外星人，再不断添加，直到没有空间添加外星人为止
        # 外星人的间距为外星人的宽度
        alien = Alien(self)

        alien_width = alien.rect.width
        alien_height = alien.rect.height

        current_x = alien_width
        current_y = alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            # print("current_x:", current_x)
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                # bili=random.randfloat(1,2)
                current_x += 2* alien_width
            current_x = alien_width
            current_y += alien_height

    def _create_alien(self, x_position, y_position):
        """创建一个外星人，并将其加入外星舰队"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """更新外星舰队中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()
        self._check_aliens_bottom()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()

    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整群外星人下移，并改变它们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def ship_hit(self):
        """响应飞船被外星人撞到"""
        self.stats.ships_left -= 1
        # 清空外星人列表和子弹列表
        self.aliens.empty()
        self.bullets.empty()
        # 创建新的舰队
        self._create_fleet()
        self.ship.center_ship()

        sleep(0.5)

    def _check_aliens_bottom(self):
        """检查是否有外星人到达了屏幕的下边缘"""
        for alien in self.aliens.sprites():

             if alien.rect.bottom >= self.settings.screen_height:
                # 像飞船被撞到一样进行处理
                self._ship_hit()
                break

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
