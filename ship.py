from __future__ import annotations

import pygame.image



class Ship:
    """飞船类"""

    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()

        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom

        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False

        self.settings=ai_game.settings
        self.x=float(self.rect.x)

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """更新飞船位置"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed
        if self.moving_up and self.rect.top>0:
            self.rect.y-=self.settings.ship_speed
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.rect.y+=self.settings.ship_speed
        self.rect.x=self.x

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)
        pass